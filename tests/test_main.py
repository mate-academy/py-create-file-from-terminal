import sys
import builtins
from datetime import datetime

from app.create_file import create_file


def run_with_args(monkeypatch, args, inputs=None):
    printed = []
    monkeypatch.setattr(sys, "argv", ["create_file.py"] + args)
    monkeypatch.setattr(builtins, "print", printed.append)

    if inputs is not None:
        it = iter(inputs)
        monkeypatch.setattr(builtins, "input", lambda _: next(it))

    create_file()
    return printed


def test_no_arguments(monkeypatch):
    output = run_with_args(monkeypatch, [])
    assert "Usage:" in "\n".join(output)


def test_only_directories(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    output = run_with_args(monkeypatch, ["-d", "dir1", "dir2"])
    dir_path = tmp_path / "dir1" / "dir2"
    assert dir_path.exists()
    assert f"Directory created at: {dir_path}" in output


def test_missing_filename_after_f(monkeypatch):
    output = run_with_args(monkeypatch, ["-f"])
    assert "Error: -f flag requires a file name" in output


def test_create_file_in_base(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    inputs = ["first line", "second line", "stop"]
    output = run_with_args(monkeypatch, ["-f", "test.txt"], inputs)

    file_path = tmp_path / "test.txt"
    assert file_path.exists()

    content = file_path.read_text(encoding="utf-8")
    lines = content.strip().splitlines()
    datetime.strptime(lines[0], "%Y-%m-%d %H:%M:%S")
    assert lines[1] == "1 first line"
    assert lines[2] == "2 second line"
    assert f"File created/updated at: {file_path}" in output


def test_create_file_in_directories(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    inputs = ["hello", "stop"]
    output = run_with_args(monkeypatch, ["-d", "dirA", "-f", "note.txt"], inputs)

    file_path = tmp_path / "dirA" / "note.txt"
    assert file_path.exists()
    content = file_path.read_text(encoding="utf-8")
    assert "1 hello" in content
    assert f"File created/updated at: {file_path}" in output
