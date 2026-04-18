import os
import shutil
from unittest.mock import patch
from app.create_file import main


def setup_module():
    """Creating a clean environment before tests."""
    for folder in ["test_folder", "dir1"]:
        if os.path.exists(folder):
            shutil.rmtree(folder)


def test_create_file_in_current_dir():
    """Check file creation without flag -d."""
    filename = "local_test.txt"
    mock_args = ["create_file.py", "-f", filename]
    mock_input = ["Line in current dir", "stop"]

    with patch("sys.argv", mock_args), patch("builtins.input", side_effect=mock_input):
        main()

    assert os.path.exists(filename) is True
    os.remove(filename)


def test_append_content():
    """Verify that data is appended to the end of the file."""
    filename = "append_test.txt"

    # First launch
    with patch("sys.argv", ["main.py", "-f", filename]), \
            patch("builtins.input", side_effect=["First line", "stop"]):
        main()

    # Second launch
    with patch("sys.argv", ["main.py", "-f", filename]), \
            patch("builtins.input", side_effect=["Second line", "stop"]):
        main()

    with open(filename, "r") as f:
        content = f.read()
        assert "1 First line" in content
        assert "1 Second line" in content

    os.remove(filename)


def test_multiple_directories():
    """Checking for creation of subfolders: -d dir1 dir2."""
    mock_args = ["create_file.py", "-d", "dir1", "dir2", "-f", "nested.txt"]
    mock_input = ["Nested content", "stop"]
    expected_path = os.path.join("dir1", "dir2", "nested.txt")

    with patch("sys.argv", mock_args), patch("builtins.input", side_effect=mock_input):
        main()

    assert os.path.exists(expected_path) is True
    shutil.rmtree("dir1")
