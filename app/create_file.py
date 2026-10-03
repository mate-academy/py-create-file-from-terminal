import os
import sys
from datetime import datetime


def parse_args(args: list) -> tuple:
    dir_parts = []
    file_names = []
    current_flag = None

    for arg in args:
        if arg in ("-d", "-f"):
            current_flag = arg
        elif current_flag == "-d":
            dir_parts.append(arg)
        elif current_flag == "-f":
            file_names.append(arg)

    file_name = file_names[0] if file_names else None
    return dir_parts, file_name


def read_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    already_has_content = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a") as file:
        if already_has_content:
            file.write("\n")
        file.write(timestamp + "\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


def create_file() -> None:
    dir_parts, file_name = parse_args(sys.argv[1:])

    if not dir_parts and file_name is None:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f file_name]")
        return

    path = ""
    if dir_parts:
        path = os.path.join(*dir_parts)
        os.makedirs(path, exist_ok=True)

    if file_name is not None:
        file_path = os.path.join(path, file_name)
        lines = read_content()
        write_to_file(file_path, lines)


if __name__ == "__main__":
    create_file()
