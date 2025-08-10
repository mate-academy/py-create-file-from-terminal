import sys
import datetime
from unittest import mock

import pytest

from app.create_file import (
    parse_command_line_args, get_date_writing,
    get_data_from_input, write_data, run
)


@pytest.fixture
def dirs_path_command_line_args() -> list[str]:
    return ["create_file_from_terminal", "-d", "dir1", "dir2"]


@pytest.fixture
def file_path_command_line_args() -> list[str]:
    return ["create_file_from_terminal", "-f", "file.txt"]


@pytest.fixture
def dirs_file_path_command_line_args() -> list[str]:
    return [
        "create_file_from_terminal", "-d", "dir1", "dir2",
        "-f", "file.txt"
    ]


@pytest.fixture
def date_writing() -> datetime.datetime:
    return datetime.datetime(2024, 9, 11, 22, 19, 5)


def test_parse_args_and_get_dirs_path(
    dirs_path_command_line_args: list[str]
) -> None:
    with mock.patch.object(sys, "argv", dirs_path_command_line_args):
        assert parse_command_line_args() == ("dir1\\dir2", "")


def test_parse_args_and_get_file_path(
    file_path_command_line_args: list[str]
) -> None:
    with mock.patch.object(sys, "argv", file_path_command_line_args):
        assert parse_command_line_args() == ("", "file.txt")


def test_parse_args_and_get_dirs_and_file_paths(
    dirs_file_path_command_line_args: list[str],
) -> None:
    with mock.patch.object(sys, "argv", dirs_file_path_command_line_args):
        assert parse_command_line_args() == ("dir1\\dir2", "file.txt")


@mock.patch("app.create_file.datetime")
def test_get_date_writing(
    mocked_datetime: mock.MagicMock,
    date_writing: datetime.datetime
) -> None:
    mocked_datetime.datetime.now.return_value = date_writing
    mocked_datetime.strftime.return_value = "2024-9-11 22:19:5"

    assert get_date_writing() == "2024-9-11 22:19:5"

    mocked_datetime.now.assert_called_once()
    mocked_datetime.strftime.assert_called_once()


@mock.patch("app.create_file.input")
def test_get_data_from_input(mocked_input: mock.MagicMock) -> None:
    mocked_input.side_effect = [
        "Line1 content",
        "Line2 content",
        "Line3 content",
        "stop"
    ]

    assert get_data_from_input() == [
        "1 Line1 content\n",
        "2 Line2 content\n",
        "3 Line3 content\n"
    ]


def test_write_data(date_writing: datetime.datetime) -> None:
    mocked_file = mock.mock_open()

    with (
        mock.patch("builtins.open", mocked_file) as mocked_open,
        mock.patch("app.create_file.datetime") as mocked_datetime
    ):
        mocked_datetime.datetime.now.return_value = date_writing
        mocked_datetime.strftime.return_value = "2024-9-11 22:19:5"

        write_data("file.txt", ["Hello", "World"])
        mocked_open.assert_called_once_with("file.txt", "a")
        mocked_file().write.assert_called_once_with("2024-9-11 22:19:5")
        mocked_file().writelines.assert_called_once_with(
            ["Hello", "World"]
        )


def test_run_make_only_dirs(
    dirs_path_command_line_args: list[str]
) -> None:
    with (
        mock.patch.object(sys, "argv", dirs_path_command_line_args),
        mock.patch("os.makedirs") as mocked_makedirs
    ):
        run()
        mocked_makedirs.assert_called_once_with("dir1\\dir2", exist_ok=True)


def test_run_make_only_file(
    file_path_command_line_args: list[str]
) -> None:
    with (
        mock.patch.object(sys, "argv", file_path_command_line_args),
        mock.patch("builtins.input") as mocked_input,
        mock.patch("app.create_file.write_data") as mocked_write_data
    ):
        mocked_input.side_effect = ["Hello", "World", "stop"]
        run()
        mocked_write_data.assert_called_once_with(
            "file.txt", ["1 Hello\n", "2 World\n"]
        )


def test_run_make_dirs_and_file(
    dirs_file_path_command_line_args: list[str]
) -> None:
    with (
        mock.patch.object(sys, "argv", dirs_file_path_command_line_args),
        mock.patch("os.makedirs") as mocked_makedirs,
        mock.patch("builtins.input") as mocked_input,
        mock.patch("app.create_file.write_data") as mocked_write_data
    ):
        mocked_input.side_effect = ["Happy birthday", "Bogdan", "stop"]
        run()
        mocked_makedirs.assert_called_once_with("dir1\\dir2", exist_ok=True)
        mocked_write_data.assert_called_once_with(
            "dir1\\dir2\\file.txt", ["1 Happy birthday\n", "2 Bogdan\n"]
        )
