import os
import tempfile
from app.create_file import create_directories, write_to_file


def test_create_directories_creates_nested_dirs(tmp_path):
    dir_path = tmp_path / "dir1" / "dir2"
    create_directories([str(dir_path)])
    assert dir_path.exists()


def test_write_to_file_creates_file(tmp_path, monkeypatch):
    test_file = tmp_path / "test.txt"

    # Симулюємо введення користувача: 2 рядки і "stop"
    inputs = iter(["Hello", "World", "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    write_to_file(str(test_file))

    content = test_file.read_text(encoding="utf-8")
    assert "Hello" in content
    assert "World" in content
