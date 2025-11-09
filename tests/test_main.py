import os
from app.create_file import create_directories, write_to_file


def test_create_directories_creates_nested_dirs(tmp_path):
    dir_parts = [str(tmp_path), "dir1", "dir2"]
    result_path = create_directories(dir_parts)
    assert os.path.exists(result_path)
    assert result_path.endswith(os.path.join("dir1", "dir2"))


def test_write_to_file_adds_timestamp_and_numbered_lines(tmp_path, monkeypatch):
    test_file = tmp_path / "test.txt"

    # Перше введення
    inputs = iter(["Hello", "World", "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    write_to_file(str(test_file))

    content_first = test_file.read_text(encoding="utf-8").strip().split("\n")
    assert len(content_first) >= 3
    assert content_first[1] == "1 Hello"
    assert content_first[2] == "2 World"
    assert "-" in content_first[0]  # timestamp у форматі 2025-11-10 00:00:00

    # Друге введення (append)
    inputs = iter(["Another", "Line", "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    write_to_file(str(test_file))

    content_second = test_file.read_text(encoding="utf-8")
    # Має бути два timestamp-блоки і порожній рядок між ними
    assert content_second.count("\n\n") >= 1
    assert "1 Another" in content_second
    assert "2 Line" in content_second
