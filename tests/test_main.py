import os
import tempfile
import sys
from unittest import mock
import pytest
from app import create_file


# Для імпорту нашого скрипта
import importlib.util

# --- helper to import create_file.py dynamically ---
def import_script(script_path):
    spec = importlib.util.spec_from_file_location("create_file", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# --- test creating directories only ---
def test_create_dirs(tmp_path):
    script_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app", "create_file.py")
    )
    dirs = ["dir1", "dir2"]

    # спочатку перейти в tmp_path
    os.chdir(tmp_path)

    # mock sys.argv
    with mock.patch("sys.argv", ["create_file.py", "-d"] + dirs):
        import_script(script_path)

    # перевірка існування директорій
    for i in range(1, len(dirs) + 1):
        path = tmp_path.joinpath(*dirs[:i])
        assert path.exists() and path.is_dir()



# --- test creating file only ---
def test_create_file_only(tmp_path):
    script_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app", "create_file.py")
    )
    file_name = "testfile.txt"

    inputs = ["Line 1", "Line 2", "stop"]
    with mock.patch("builtins.input", side_effect=inputs):
        with mock.patch("sys.argv", ["create_file.py", "-f", file_name]):
            os.chdir(tmp_path)
            import_script(script_path)

    file_path = tmp_path / file_name
    assert file_path.exists()
    content = file_path.read_text()
    for line in ["1 Line 1", "2 Line 2"]:
        assert line in content


# --- test creating directories + file inside ---
def test_create_dirs_and_file(tmp_path):
    script_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app", "create_file.py")
    )
    dirs = ["dirA", "dirB"]
    file_name = "file.txt"
    inputs = ["Hello", "World", "stop"]

    with mock.patch("builtins.input", side_effect=inputs):
        with mock.patch("sys.argv", ["create_file.py", "-d"] + dirs + ["-f", file_name]):
            os.chdir(tmp_path)
            import_script(script_path)

    file_path = tmp_path.joinpath(*dirs, file_name)
    assert file_path.exists()
    content = file_path.read_text()
    for line in ["1 Hello", "2 World"]:
        assert line in content


def test_append_file_content(tmp_path):
    script_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app", "create_file.py")
    )
    file_name = "append_test.txt"

    # first run
    inputs1 = ["First line", "stop"]
    os.chdir(tmp_path)
    with mock.patch("builtins.input", side_effect=inputs1):
        with mock.patch("sys.argv", ["create_file.py", "-f", file_name]):
            import_script(script_path)

    # second run
    inputs2 = ["Second line", "stop"]
    with mock.patch("builtins.input", side_effect=inputs2):
        with mock.patch("sys.argv", ["create_file.py", "-f", file_name]):
            import_script(script_path)

    # verify content
    file_path = tmp_path / file_name
    content = file_path.read_text()
    # should contain both blocks separated by a single blank line
    assert "1 First line" in content
    assert "1 Second line" in content
    assert content.count("\n\n") == 1  # only one blank line separator
