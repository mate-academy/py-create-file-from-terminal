import os
import re
from unittest.mock import patch

import pytest

from app.create_file import (
    parse_args,
    ensure_dirs,
    collect_lines,
    append_block,
)


def _mock_inputs(seq):
    it = iter(seq)
    return lambda _: next(it)


def test_parse_args_dirs_only():
    dparts, fname = parse_args(["-d", "dir1", "dir2"])
    assert dparts == ["dir1", "dir2"]
    assert fname is None


def test_parse_args_file_only():
    dparts, fname = parse_args(["-f", "file.txt"])
    assert dparts == []
    assert fname == "file.txt"


def test_parse_args_dirs_and_file():
    dparts, fname = parse_args(["-d", "a", "b", "-f", "x.txt"])
    assert dparts == ["a", "b"]
    assert fname == "x.txt"


def test_parse_args_errors():
    with pytest.raises(SystemExit):
        parse_args([])

    with pytest.raises(SystemExit):
        parse_args(["-d"])

    with pytest.raises(SystemExit):
        parse_args(["-f"])

    with pytest.raises(SystemExit):
        parse_args(["-f", "a.txt", "-f", "b.txt"])

    with pytest.raises(SystemExit):
        parse_args(["--oops"])


def test_ensure_dirs_creates_nested(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    base = ensure_dirs(["dir1", "dir2"])
    assert os.path.isdir(base)
    assert base.endswith(os.path.join("dir1", "dir2"))


def test_collect_lines_exact_stop_only():
    inputs = ["Line1", "Stop", "STOP", " stop ", "Line2", "stop"]
    with patch("builtins.input", side_effect=_mock_inputs(inputs)):
        lines = collect_lines()
    # Only exact "stop" terminates; variants are kept as content
    assert lines == ["Line1", "Stop", "STOP", " stop ", "Line2"]


def test_append_block_creates_and_appends(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    file_path = tmp_path / "file.txt"

    # First write
    append_block(str(file_path), ["A", "B", "C"])
    text1 = file_path.read_text(encoding="utf-8")
    first_line = text1.splitlines()[0]
    assert re.match(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}$", first_line)
    assert "1 A" in text1 and "2 B" in text1 and "3 C" in text1

    # Second write (appends with blank line)
    append_block(str(file_path), ["X", "Y"])
    text2 = file_path.read_text(encoding="utf-8")
    assert "\n\n" in text2
    blocks = text2.strip().split("\n\n")
    assert len(blocks) == 2

    second = blocks[1].splitlines()
    assert re.match(r"\d{4}-\d{2}-\d2\s\d{2}:\d{2}:\d{2}$", second[0]) or \
           re.match(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}$", second[0])
    assert second[1] == "1 X"
    assert second[2] == "2 Y"


def test_append_block_empty_input_creates_empty_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    p = tmp_path / "empty.txt"
    append_block(str(p), [])
    assert p.exists()
    assert p.read_text(encoding="utf-8") == ""
