import os
import copy

import pytest
from pytest import MonkeyPatch

import app.create_file as create_file


class CleanUpFile:
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        path_components = self.filename.split("/")
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
                "dir1/dir2/test_file",
                ["HI", "There", "stop"]
        ),
        (
                ["-f", "test_file", "-d", "dir3", "dir4"],
                "dir3/dir4/test_file",
                ["HI", "There", "stop"]
        ),
        (
                ["-f", "test_file"],
                "test_file",
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
    file_path: str,
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
                "dir5/dir6/"
        ),
    ],
    ids=[
        "only -d flag"
    ]
)
def test_create_folder_with_only_d_flag(
    monkeypatch: MonkeyPatch,
    terminal_arguments: list,
    file_path: str
):
    monkeypatch.setattr("sys.argv", terminal_arguments)

    with CleanUpFile(file_path):
        create_file.main()

        assert os.path.exists(file_path)