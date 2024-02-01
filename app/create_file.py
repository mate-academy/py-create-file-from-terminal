import os
import sys
from datetime import datetime


def main() -> None:
    directories = get_flag_args("-d")
    if directories:
        create_directory(directories)

    filenames = get_flag_args("-f")
    if filenames:
        filename = filenames[0]
        lines = read_lines()
        write_to_file(directories, filename, lines)


def get_flag_args(flag: str) -> list:
    if flag not in sys.argv:
        return []
    args = []
    for i in range(sys.argv.index(flag) + 1, len(sys.argv)):
        if sys.argv[i].startswith("-"):
            break
        args.append(sys.argv[i])
    return args


def create_directory(directories: list) -> None:
    path = os.path.join(*directories)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def write_to_file(directories: list, filename: str, lines: list) -> None:
    file_path = os.path.join(*directories, filename)
    with open(file_path, "a") as source_file:
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{current_date}\n")
        for i in range(len(lines)):
            source_file.write(f"{i + 1} {lines[i]}\n")
        source_file.write("\n")


def read_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines
