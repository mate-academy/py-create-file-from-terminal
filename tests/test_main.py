from app.create_file import parse_args

def test_parse_args_only_f():
    args = ["-f", "note.txt"]
    dirs, fname = parse_args(args)
    assert dirs == []
    assert fname == "note.txt"