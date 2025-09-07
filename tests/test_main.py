import os
from datetime import datetime
from app.create_file import parse_arguments, ensure_directories, append_block


def test_parse_arguments_with_dir_and_file():
    args = ["-d", "dir1", "dir2", "-f", "file.txt"]
    dirs, filename = parse_arguments(args)
    assert dirs == ["dir1", "dir2"]
    assert filename == "file.txt"


def test_parse_arguments_only_dir():
    args = ["-d", "dir1", "dir2"]
    dirs, filename = parse_arguments(args)
    assert dirs == ["dir1", "dir2"]
    assert filename is None


def test_parse_arguments_only_file():
    args = ["-f", "file.txt"]
    dirs, filename = parse_arguments(args)
    assert dirs == []
    assert filename == "file.txt"


def test_ensure_directories_creates_path(tmp_path):
    parts = [tmp_path, "a", "b"]
    path = ensure_directories(parts)
    assert os.path.exists(path)
    assert os.path.isdir(path)


def test_append_block_creates_and_appends(tmp_path):
    file_path = tmp_path / "file.txt"
    # перший блок
    append_block(str(file_path), ["line1", "line2"])
    content = file_path.read_text().strip().splitlines()
    assert "1 line1" in content
    assert "2 line2" in content

    # другий блок
    append_block(str(file_path), ["line3"])
    content2 = file_path.read_text().strip().splitlines()
    # другий блок теж має починатись із timestamp і мати "1 line3"
    assert any("1 line3" in line for line in content2)


def test_append_block_has_timestamp(tmp_path):
    file_path = tmp_path / "file.txt"
    append_block(str(file_path), ["abc"])
    first_line = file_path.read_text().splitlines()[0]
    # формат YYYY-MM-DD HH:MM:SS
    datetime.strptime(first_line, "%Y-%m-%d %H:%M:%S")
