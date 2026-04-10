import os
import shutil
from datetime import datetime
from unittest.mock import patch
from app.create_file import main


def cleanup() -> None:
    for item in ["dir1", "file.txt"]:
        if os.path.isdir(item):
            shutil.rmtree(item)
        elif os.path.isfile(item):
            os.remove(item)


def test_create_dir_and_file() -> None:
    cleanup()
    test_args = ["app/create_file.py", "-d", "dir1", "dir2", "-f", "file.txt"]
    test_input = ["Line1 content", "Line2 content", "stop"]

    with patch("sys.argv", test_args), patch("builtins.input", side_effect=test_input):
        main()

    path = os.path.join("dir1", "dir2", "file.txt")
    assert os.path.exists(path), (
        f"File {path} should exist in the created directory hierarchy"
    )

    with open(path, "r") as source_file:
        lines = source_file.readlines()
        # Verify timestamp format
        try:
            datetime.strptime(lines[0].strip(), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            assert False, (
                f"Invalid timestamp format: '{lines[0].strip()}'. "
                f"Expected format: YYYY-MM-DD HH:MM:SS"
            )

        assert lines[1].strip() == "1 Line1 content", (
            f"Line 1 mismatch: expected '1 Line1 content', got '{lines[1].strip()}'"
        )
        assert lines[2].strip() == "2 Line2 content", (
            f"Line 2 mismatch: expected '2 Line2 content', got '{lines[2].strip()}'"
        )
    cleanup()


def test_create_file_and_dirs_reversed() -> None:
    cleanup()
    test_args = [
        "app/create_file.py",
        "-f",
        "file.txt",
        "-d",
        "dir1",
        "dir2",
        "dir3",
        "dir4",
    ]
    test_input = ["Line1", "stop"]

    with patch("sys.argv", test_args), patch("builtins.input", side_effect=test_input):
        main()

    path = os.path.join("dir1", "dir2", "dir3", "dir4", "file.txt")
    assert os.path.exists(path), (
        f"File {path} should be created even when -f flag is passed before -d"
    )
    cleanup()


def test_create_only_file() -> None:
    cleanup()
    test_args = ["app/create_file.py", "-f", "file.txt"]
    test_input = ["Content line", "stop"]

    with patch("sys.argv", test_args), patch("builtins.input", side_effect=test_input):
        main()

    assert os.path.exists("file.txt"), (
        "File 'file.txt' should be created in the current directory "
        "when no directories are specified"
    )
    cleanup()


def test_create_only_dirs() -> None:
    cleanup()
    test_args = ["app/create_file.py", "-d", "dir1", "dir2", "dir3", "dir4"]

    with patch("sys.argv", test_args):
        main()

    path = os.path.join("dir1", "dir2", "dir3", "dir4")
    assert os.path.isdir(path), (
        f"Directory {path} should be created when only -d flag is provided"
    )
    cleanup()


def test_append_with_blank_line() -> None:
    cleanup()
    # First entry
    with (
        patch("sys.argv", ["app/create_file.py", "-f", "file.txt"]),
        patch("builtins.input", side_effect=["Line 1", "stop"]),
    ):
        main()

    # Second entry
    with (
        patch("sys.argv", ["app/create_file.py", "-f", "file.txt"]),
        patch("builtins.input", side_effect=["Line 2", "stop"]),
    ):
        main()

    with open("file.txt", "r") as source_file:
        content = source_file.read()

    # Check for blank line between entries
    parts = content.split("\n\n")
    assert len(parts) == 2, (
        f"Expected exactly 2 entries separated by a blank line, but found {len(parts)}"
    )

    # Check first entry
    lines1 = parts[0].split("\n")
    assert lines1[1] == "1 Line 1", (
        f"First entry content mismatch: expected '1 Line 1', got '{lines1[1]}'"
    )

    # Check second entry
    lines2 = parts[1].split("\n")
    assert lines2[1] == "1 Line 2", (
        f"Second entry content mismatch: expected '1 Line 2', got '{lines2[1]}'"
    )
    cleanup()


def test_stop_word() -> None:
    cleanup()
    # Test that it stops exactly at "stop"
    test_args = ["app/create_file.py", "-f", "file.txt"]
    test_input = ["line", "stop", "extra"]

    with patch("sys.argv", test_args), patch("builtins.input", side_effect=test_input):
        main()

    with open("file.txt", "r") as source_file:
        lines = source_file.readlines()
        assert len(lines) == 2, (
            "File should contain exactly 2 lines "
            "(timestamp and 1 content line), "
            f"but has {len(lines)}"
        )
        assert lines[1].strip() == "1 line", (
            f"Content line mismatch: expected '1 line', got '{lines[1].strip()}'"
        )
    cleanup()


def test_input_prompt() -> None:
    cleanup()
    test_args = ["app/create_file.py", "-f", "file.txt"]
    test_input = ["line 1", "stop"]

    with (
        patch("sys.argv", test_args),
        patch("builtins.input", side_effect=test_input) as mock_input,
    ):
        main()

        assert mock_input.call_args_list[0][0][0] == "Enter content line: ", (
            f"Expected prompt 'Enter content line: ', but got '{mock_input.call_args_list[0][0][0]}'"
        )
        assert mock_input.call_args_list[1][0][0] == "Enter content line: ", (
            f"Expected prompt 'Enter content line: ' for the stop command as well, "
            f"but got '{mock_input.call_args_list[1][0][0]}'"
        )
    cleanup()
