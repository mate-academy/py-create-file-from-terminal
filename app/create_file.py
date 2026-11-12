import os
import sys
from datetime import datetime


def parse_args(args: list) -> tuple:
    dir_parts = []
    file_name = None

    if "-d" in args:
        index = args.index("-d") + 1
        while index >= 0:
            dir_parts.append(args[index])
            index -= 1

    if "-f" in args:
        index = args.index("-f") + 1
        if index < len(args):
            file_name += args[index]

    return dir_parts, file_name


def get_content_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
        return lines


def write_to_file(path: str) -> None:
    lines = get_content_lines()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(path)

    with open(path, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(timestamp + "\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


def create_file() -> None:
    dir_parts, file_name = parse_args(sys.argv[1:])

    directory = ""
    if dir_parts:
        directory = os.path.join(*dir_parts)
        os.makedirs(directory, exist_ok=True)

    if file_name:
        write_to_file(os.path.join(directory, file_name))


if __name__ == "__main__":
    create_file()
