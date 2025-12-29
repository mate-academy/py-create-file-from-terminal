import os
import copy

import pytest
from pytest import MonkeyPatch

import app.create_file as create_file


class CleanUpFile:
    def __init__(self, filename: str | bytes):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        path_components = self.filename.split(os.path.sep)
        for _ in range(len(path_components)):
            remaining_path = os.path.join(*path_components)
            if not os.path.exists(remaining_path):
                break

            if os.path.isfile(remaining_path):
                os.remove(remaining_path)

            if os.path.isdir(remaining_path):
                os.rmdir(remaining_path)

            path_components.pop(-1)


@pytest.mark.parametrize(
    "terminal_arguments, file_path, content",
    [
        (
                ["-d", "dir1", "dir2", "-f", "test_file"],
                ["dir1", "dir2", "test_file"],
                ["HI", "There", "stop"]
        ),
        (
                ["-f", "test_file", "-d", "dir3", "dir4"],
                ["dir3", "dir4", "test_file"],
                ["HI", "There", "stop"]
        ),
        (
                ["-f", "test_file"],
                ["test_file"],
                ["HI", "There", "stop"]
        )
    ],
    ids=[
        "-d flag before -f flag",
        "-d flag after -f flag",
        "only -f flag"
    ]
)
def test_create_file_with_flags(
    monkeypatch: MonkeyPatch,
    terminal_arguments: list,
    file_path: list[str],
    content: list[str]
):
    inputs = copy.copy(content)
    input_messages = []
    current_time = create_file.datetime.now()
    file_path = os.path.join(*file_path)

    def mock_input_content(text):
        input_messages.append(text)
        return inputs.pop(0)

    monkeypatch.setattr("sys.argv", terminal_arguments)
    monkeypatch.setattr("builtins.input", mock_input_content)
    monkeypatch.setattr("app.create_file.datetime", current_time)

    with CleanUpFile(file_path):
        create_file.main()

        assert input_messages == (["Enter content line: "] * len(content))

        assert os.path.exists(file_path)

        with open(file_path, "r") as f:
            for i in range(len(content) - 1):
                content[i] = f"{i + 1} {content[i]}"
            generated_content = f.read().splitlines()
            assert generated_content[0] == current_time.strftime("%Y-%m-%d %H:%M:%S")
            assert generated_content[1:] == content[:-1]


@pytest.mark.parametrize(
    "terminal_arguments, file_path",
    [
        (
                ["-d", "dir5", "dir6"],
                ["dir5", "dir6"]
        ),
    ],
    ids=[
        "only -d flag"
    ]
)
def test_create_folder_with_only_d_flag(
    monkeypatch: MonkeyPatch,
    terminal_arguments: list,
    file_path: list[str]
):
    assert file_path, "file_path must not be empty"
    file_path = os.path.join(*file_path)
    monkeypatch.setattr("sys.argv", terminal_arguments)

    with CleanUpFile(file_path):
        create_file.main()

        assert os.path.exists(file_path)


@pytest.fixture()
def test_folder():
    lines = ["2025-12-29 15:56:11\n", "1 hi\n", "2 there\n"]
    os.makedirs("append/test")
    with open("append/test/test_file", "w") as f:
        f.writelines(lines)
    return os.path.relpath("append/test/test_file")


@pytest.mark.parametrize(
    "terminal_arguments, content",
    [
        (
                ["-d", "append", "test", "-f", "test_file"],
                ["HI", "There", "stop"]
        )
    ],
    ids=[
        "append"
    ]
)
def test_append_functionality(
    test_folder,
    monkeypatch: MonkeyPatch,
    terminal_arguments: list,
    content: list[str]
):
    inputs = copy.copy(content)
    input_messages = []
    current_time = create_file.datetime.now()

    def mock_input_content(text):
        input_messages.append(text)
        return inputs.pop(0)

    monkeypatch.setattr("sys.argv", terminal_arguments)
    monkeypatch.setattr("builtins.input", mock_input_content)
    monkeypatch.setattr("app.create_file.datetime", current_time)

    with open(test_folder, "r") as f:
        length_before_append = len(f.readlines())

    create_file.main()

    assert input_messages == (["Enter content line: "] * len(content))
    assert os.path.exists(test_folder)

    with CleanUpFile(test_folder):
        with open(test_folder, "r") as f:
            all_lines = f.readlines()
            assert len(all_lines) > length_before_append

            for i in range(len(content) - 1):
                content[i] = f"{i + 1} {content[i]}"

            new_content_start = length_before_append
            assert all_lines[new_content_start].strip() == ""
            assert (
                all_lines[new_content_start + 1].strip() == current_time.strftime("%Y-%m-%d %H:%M:%S")
            )

            for i, expected_line in enumerate(content[:-1]):
                actual_line = all_lines[new_content_start + 2 + i].strip()
                assert actual_line == expected_line
