import pytest
from app.create_file import find_path_and_filename

def test_dirs_only(monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(
        "sys.argv",
        ["app.py", "-d", "a", "b", "c"]
    )

    result = find_path_and_filename()

    assert result is None
    assert (tmp_path / "a" / "b" / "c").exists()

