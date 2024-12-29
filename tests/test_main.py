import os
import pytest


@pytest.fixture
def temp_dir(tmp_path: str) -> str:
    return tmp_path


def test_directory_tree_creation(temp_dir: str) -> None:
    os.makedirs(temp_dir / "subdir1" / "subdir2")
    assert (temp_dir / "subdir1" / "subdir2").is_dir()


def test_file_creation_in_directory(temp_dir: str) -> None:
    file_path = temp_dir / "test_file.txt"
    file_path.touch()
    assert file_path.is_file()


def test_content_addition_to_file(temp_dir: str) -> None:
    file_path = temp_dir / "test_file.txt"
    content = [
        "2022-02-01 14:46:01",
        "1 Line1 content",
        "2 Line2 content",
        "3 Line3 content"
    ]
    file_path.write_text("\n".join(content) + "\n")
    with open(file_path, "r") as f:
        lines = f.readlines()
    assert lines == [line + "\n" for line in content]
