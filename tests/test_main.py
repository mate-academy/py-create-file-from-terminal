import os
import runpy
import shutil
from datetime import datetime
from unittest.mock import patch

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCRIPT_PATH = os.path.join(BASE_DIR, "app", "create_file.py")

def cleanup() -> None:
    for item in ["dir1", "file.txt"]:
        if os.path.isdir(item):
            shutil.rmtree(item)
        elif os.path.isfile(item):
            os.remove(item)

def test_create_dir_and_file() -> None:
    cleanup()
    test_args = [SCRIPT_PATH, "-d", "dir1", "dir2", "-f", "file.txt"]
    test_input = ["Line1 content", "Line2 content", "stop"]

    with patch("sys.argv", test_args), patch("builtins.input", side_effect=test_input):
        runpy.run_path(SCRIPT_PATH, run_name="__main__")

    path = os.path.join("dir1", "dir2", "file.txt")
    assert os.path.exists(path)

    with open(path, "r") as source_file:
        lines = source_file.readlines()
        try:
            datetime.strptime(lines[0].strip(), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            assert False

        assert lines[1].strip() == "1 Line1 content"
        assert lines[2].strip() == "2 Line2 content"
    cleanup()

def test_create_file_and_dirs_reversed() -> None:
    cleanup()
    test_args = [SCRIPT_PATH, "-f", "file.txt", "-d", "dir1", "dir2", "dir3", "dir4"]
    test_input = ["Line1", "stop"]

    with patch("sys.argv", test_args), patch("builtins.input", side_effect=test_input):
        runpy.run_path(SCRIPT_PATH, run_name="__main__")

    path = os.path.join("dir1", "dir2", "dir3", "dir4", "file.txt")
    assert os.path.exists(path)
    cleanup()

def test_create_only_file() -> None:
    cleanup()
    test_args = [SCRIPT_PATH, "-f", "file.txt"]
    test_input = ["Content line", "stop"]

    with patch("sys.argv", test_args), patch("builtins.input", side_effect=test_input):
        runpy.run_path(SCRIPT_PATH, run_name="__main__")

    assert os.path.exists("file.txt")
    cleanup()

def test_create_only_dirs() -> None:
    cleanup()
    test_args = [SCRIPT_PATH, "-d", "dir1", "dir2", "dir3", "dir4"]

    with patch("sys.argv", test_args):
        runpy.run_path(SCRIPT_PATH, run_name="__main__")

    path = os.path.join("dir1", "dir2", "dir3", "dir4")
    assert os.path.isdir(path)
    cleanup()

def test_append_with_blank_line() -> None:
    cleanup()
    with (
        patch("sys.argv", [SCRIPT_PATH, "-f", "file.txt"]),
        patch("builtins.input", side_effect=["Line 1", "stop"]),
    ):
        runpy.run_path(SCRIPT_PATH, run_name="__main__")

    with (
        patch("sys.argv", [SCRIPT_PATH, "-f", "file.txt"]),
        patch("builtins.input", side_effect=["Line 2", "stop"]),
    ):
        runpy.run_path(SCRIPT_PATH, run_name="__main__")

    with open("file.txt", "r") as source_file:
        content = source_file.read()

    parts = content.split("\n\n")
    assert len(parts) == 2
    assert "1 Line 1" in parts[0]
    assert "1 Line 2" in parts[1]
    cleanup()

def test_stop_word() -> None:
    cleanup()
    test_args = [SCRIPT_PATH, "-f", "file.txt"]
    test_input = ["line", "stop", "extra"]

    with patch("sys.argv", test_args), patch("builtins.input", side_effect=test_input):
        runpy.run_path(SCRIPT_PATH, run_name="__main__")

    with open("file.txt", "r") as source_file:
        lines = source_file.readlines()
        assert len(lines) == 2
        assert lines[1].strip() == "1 line"
    cleanup()

def test_input_prompt() -> None:
    cleanup()
    test_args = [SCRIPT_PATH, "-f", "file.txt"]
    test_input = ["line 1", "stop"]

    with (
        patch("sys.argv", test_args),
        patch("builtins.input", side_effect=test_input) as mock_input,
    ):
        runpy.run_path(SCRIPT_PATH, run_name="__main__")

        assert mock_input.call_args_list[0][0][0] == "Enter content line: "
        assert mock_input.call_args_list[1][0][0] == "Enter content line: "
    cleanup()