import os
from app.create_file import create_file

def test_create_file_only_flag_f(tmp_path):
    tmpdir = str(tmp_path)
    args = ["-f", os.path.join(tmpdir, "out.txt")]
    input_lines = ["Hello", "World"]
    filepath = create_file(args, input_lines)

    assert os.path.exists(filepath)
    with open(filepath, encoding="utf-8") as f:
        content = f.read().splitlines()

    assert content[0].count("-") == 2
    assert content[1].startswith("1 Hello")
    assert content[2].startswith("2 World")
