import os
import sys
import pytest
from datetime import datetime
from app.create_file import make_dirs, create_file, main


def test_make_dirs_empty(tmp_path):
    result = make_dirs(tmp_path, [])
    assert result == str(tmp_path)
    assert os.path.exists(result)


def test_make_dirs_multiple(tmp_path):
    dirs = ["dir1", "dir2"]
    result = make_dirs(tmp_path, ["-d"] + dirs)
    expected_path = os.path.join(tmp_path, *dirs)
    assert result == expected_path
    assert os.path.exists(expected_path)


def test_create_file_add_lines(tmp_path, monkeypatch):
    file_name = "test_file.txt"
    full_path = os.path.join(tmp_path, file_name)
    lines_to_input = ["Line1", "Line2", "stop"]
    inputs = iter(lines_to_input)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    create_file(["-f", file_name], str(tmp_path))
    assert os.path.exists(full_path)
    content = open(full_path).read().splitlines()
    datetime.strptime(content[0], "%Y-%m-%d %H:%M:%S")
    assert content[1] == "1 Line1"
    assert content[2] == "2 Line2"


def test_create_file_append_block(tmp_path, monkeypatch):
    file_name = "append_test.txt"
    full_path = os.path.join(tmp_path, file_name)
    inputs1 = iter(["First1", "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs1))
    create_file(["-f", file_name], str(tmp_path))
    inputs2 = iter(["Second1", "Second2", "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs2))
    create_file(["-f", file_name], str(tmp_path))
    content = open(full_path).read().splitlines()
    assert content[0] != "" and content[3] == ""
    assert "1 Second1" in content
    assert "2 Second2" in content


def test_create_file_with_none(monkeypatch):
    with pytest.raises(TypeError):
        create_file(None, "")


def test_make_dirs_with_none():
    with pytest.raises(TypeError):
        make_dirs("", None)


def test_make_dirs_single_directory(tmp_path):
    result = make_dirs(tmp_path, ["-d", "single_dir"])
    expected_path = os.path.join(tmp_path, "single_dir")
    assert result == expected_path
    assert os.path.exists(expected_path)


def test_make_dirs_with_file_flag(tmp_path):
    result = make_dirs(tmp_path, ["-d", "dir1", "dir2", "-f", "file.txt"])
    expected_path = os.path.join(tmp_path, "dir1", "dir2")
    assert result == expected_path
    assert os.path.exists(expected_path)


def test_make_dirs_already_exists(tmp_path):
    dirs = ["existing_dir"]
    first_result = make_dirs(tmp_path, ["-d"] + dirs)
    second_result = make_dirs(tmp_path, ["-d"] + dirs)
    assert first_result == second_result
    assert os.path.exists(second_result)


def test_create_file_immediate_stop(tmp_path, monkeypatch):
    file_name = "empty_content.txt"
    full_path = os.path.join(tmp_path, file_name)
    inputs = iter(["stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    create_file(["-f", file_name], str(tmp_path))
    assert os.path.exists(full_path)
    content = open(full_path).read().splitlines()
    assert len(content) == 1
    datetime.strptime(content[0], "%Y-%m-%d %H:%M:%S")


def test_create_file_case_insensitive_stop(tmp_path, monkeypatch):
    file_name = "case_test.txt"
    full_path = os.path.join(tmp_path, file_name)
    inputs = iter(["Line1", "STOP"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    create_file(["-f", file_name], str(tmp_path))
    content = open(full_path).read().splitlines()
    assert "1 Line1" in content
    assert "STOP" not in content


def test_make_dirs_three_levels(tmp_path):
    dirs = ["level1", "level2", "level3"]
    result = make_dirs(tmp_path, ["-d"] + dirs)
    expected_path = os.path.join(tmp_path, *dirs)
    assert result == expected_path
    assert os.path.exists(expected_path)


def test_main_only_directories(tmp_path, monkeypatch):
    test_args = ["create_file.py", "-d", "test_dir1", "test_dir2"]
    monkeypatch.setattr("sys.argv", test_args)
    monkeypatch.setattr("app.create_file.os.path.abspath", lambda x: str(tmp_path))
    monkeypatch.setattr("app.create_file.os.path.dirname", lambda x: str(tmp_path))

    main()

    expected_path = os.path.join(tmp_path, "test_dir1", "test_dir2")
    assert os.path.exists(expected_path)


def test_main_only_file(tmp_path, monkeypatch):
    test_args = ["create_file.py", "-f", "test.txt"]
    inputs = iter(["Test line", "stop"])
    monkeypatch.setattr("sys.argv", test_args)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("app.create_file.os.path.abspath", lambda x: str(tmp_path))
    monkeypatch.setattr("app.create_file.os.path.dirname", lambda x: str(tmp_path))

    main()

    full_path = os.path.join(tmp_path, "test.txt")
    assert os.path.exists(full_path)
    content = open(full_path).read()
    assert "Test line" in content


def test_main_both_flags(tmp_path, monkeypatch):
    test_args = ["create_file.py", "-d", "dir1", "dir2", "-f", "file.txt"]
    inputs = iter(["Line1", "Line2", "stop"])
    monkeypatch.setattr("sys.argv", test_args)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("app.create_file.os.path.abspath", lambda x: str(tmp_path))
    monkeypatch.setattr("app.create_file.os.path.dirname", lambda x: str(tmp_path))

    main()

    dir_path = os.path.join(tmp_path, "dir1", "dir2")
    file_path = os.path.join(dir_path, "file.txt")
    assert os.path.exists(dir_path)
    assert os.path.exists(file_path)
    content = open(file_path).read()
    assert "Line1" in content
    assert "Line2" in content


def test_main_no_flags(tmp_path, monkeypatch):
    test_args = ["create_file.py"]
    monkeypatch.setattr("sys.argv", test_args)
    monkeypatch.setattr("app.create_file.os.path.abspath", lambda x: str(tmp_path))
    monkeypatch.setattr("app.create_file.os.path.dirname", lambda x: str(tmp_path))

    main()
