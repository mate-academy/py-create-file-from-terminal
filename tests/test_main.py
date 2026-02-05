import os
import datetime
import tempfile
import pytest

from app.create_file import create_directory, create_file


def test_create_directory():
    with tempfile.TemporaryDirectory() as tmp_dir:
        dir_path = os.path.join(tmp_dir, "test_dir")
        create_directory([dir_path])
        assert os.path.exists(dir_path)


def test_create_file():
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = os.path.join(tmp_dir, "test_file.txt")
        create_file("test_file.txt", [tmp_dir])
        assert os.path.exists(file_path)


def test_create_file_with_content():
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = os.path.join(tmp_dir, "test_file.txt")
        content = "Line1 content\nLine2 content\nstop"
        create_file("test_file.txt", [tmp_dir])
        with open(file_path, "r") as file:
            file_content = file.read()
        expected_content = (
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n" +
            "1 Line1 content \n" +
            "2 Line2 content \n"
        )
        assert file_content == expected_content


def test_create_directory_and_file():
    with tempfile.TemporaryDirectory() as tmp_dir:
        dir_path = os.path.join(tmp_dir, "test_dir")
        file_path = os.path.join(dir_path, "test_file.txt")
        content = "Line1 content\nstop"
        create_directory([dir_path])
        create_file("test_file.txt", [dir_path])
        with open(file_path, "r") as file:
            file_content = file.read()
        expected_content = (
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n" +
            "1 Line1 content \n"
        )
        assert file_content == expected_content


if __name__ == "__main__":
    pytest.main([__file__])
