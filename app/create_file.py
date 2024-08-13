import os

import sys

from datetime import datetime


def get_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, content_lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(f"{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        directory = os.path.join(*args[d_index + 1:])
        os.makedirs(directory, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        if "-d" in args:
            file_path = os.path.join(directory, file_name)
        else:
            file_path = file_name

    content_lines = get_content()
    write_to_file(file_path, content_lines)
