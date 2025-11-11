from app.create_file import create_file
import os
import re


def test_create_file_creates_new_file(tmp_path):
    dir_parts = [str(tmp_path)]
    file_name = "output.txt"
    lines = ["first line", "second line"]

    file_path = create_file(dir_parts, file_name, lines)

    assert os.path.exists(file_path)

    content = open(file_path, encoding="utf-8").read().strip().split("\n")
    assert re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", content[0])
    assert content[1] == "1 first line"
    assert content[2] == "2 second line"


def test_create_file_appends_to_existing_file(tmp_path):
    dir_parts = [str(tmp_path)]
    file_name = "existing.txt"
    initial_lines = ["initial"]
    updated_lines = ["new line"]

    file_path = create_file(dir_parts, file_name, initial_lines)
    file_path = create_file(dir_parts, file_name, updated_lines)

    content = open(file_path, encoding="utf-8").read().strip().split("\n")

    # Expect two timestamp blocks
    timestamps = [line for line in content if re.match(r"\d{4}-\d{2}-\d{2}", line)]
    assert len(timestamps) == 2
    assert "1 initial" in content
    assert "1 new line" in content


def test_create_file_creates_nested_directory(tmp_path):
    nested_dir = tmp_path / "level1" / "level2"
    dir_parts = [str(nested_dir)]
    file_name = "nested.txt"
    lines = ["inside nested"]

    file_path = create_file(dir_parts, file_name, lines)

    assert os.path.exists(file_path)
    assert "inside nested" in open(file_path, encoding="utf-8").read()
