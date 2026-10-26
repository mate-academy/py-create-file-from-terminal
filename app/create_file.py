import os
import sys
from datetime import datetime


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    dirs = []
    file_name = None
    mode = None
    for arg in args:
        if arg == "-d":
            mode = "d"
        elif arg == "-f":
            mode = "f"
        elif mode == "d":
            dirs.append(arg)
        elif mode == "f" and file_name is None:
            file_name = arg
    return dirs, file_name


def read_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def create_file() -> None:
    dirs, file_name = parse_args(sys.argv[1:])

    if not dirs and file_name is None:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f file_name]")
        return

    path = os.getcwd()
    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)

    if file_name is None:
        return

    file_path = os.path.join(path, file_name)
    lines = read_content()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    separator = ""
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        separator = "\n"

    with open(file_path, "a") as f:
        f.write(separator + timestamp + "\n")
        for number, line in enumerate(lines, 1):
            f.write(f"{number} {line}\n")


create_file()
