"""Tests for create_file.py."""

from pathlib import Path
from app import create_file


def test_create_directories(tmp_path):
    """Test that nested directories are created correctly."""
    dir_path = tmp_path / "dir1" / "dir2"
    create_file.create_directories([str(dir_path)])
    assert dir_path.exists()
    assert dir_path.is_dir()


def test_write_to_file(tmp_path):
    """Test writing lines to a file with timestamp."""
    file_path = tmp_path / "example.txt"
    lines = ["line1", "line2"]

    create_file.write_to_file(file_path, lines)

    content = file_path.read_text(encoding="utf-8")
    assert "line1" in content
    assert "line2" in content
    assert "Created:" in content
    assert content.count("\n") > 2


def test_get_content_from_user(monkeypatch):
    """Test that user input stops when 'stop' is entered."""
    inputs = iter(["строка 1", "строка 2", "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = create_file.get_content_from_user()
    assert result == ["строка 1", "строка 2"]
