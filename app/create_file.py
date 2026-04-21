import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def get_content_lines() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def create_file(path: str, filename: str) -> None:
    filepath = os.path.join(path, filename)
    lines = get_content_lines()
    exists = os.path.exists(filepath)
    mode = "a" if exists else "w"
    with open(filepath, mode) as f:
        if exists:
            f.write("\n")
        f.write(get_timestamp() + "\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    directory = "."
    filename = None

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")
        if d_index < f_index:
            dir_parts = args[d_index + 1:f_index]
            filename = args[f_index + 1]
        else:
            filename = args[f_index + 1]
            dir_parts = args[d_index + 1:]
        directory = os.path.join(*dir_parts)
        create_directory(directory)
    elif "-d" in args:
        d_index = args.index("-d")
        dir_parts = args[d_index + 1:]
        directory = os.path.join(*dir_parts)
        create_directory(directory)
    elif "-f" in args:
        f_index = args.index("-f")
        filename = args[f_index + 1]

    if filename:
        create_file(directory, filename)


main()
