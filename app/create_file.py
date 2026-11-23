import os
import sys
from datetime import datetime


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    directories = []
    file_name = None
    mode = None

    for arg in args:
        if arg == "-d":
            mode = "d"
        elif arg == "-f":
            mode = "f"
        elif mode == "d":
            directories.append(arg)
        elif mode == "f" and file_name is None:
            file_name = arg

    return directories, file_name


def read_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def create_file() -> None:
    directories, file_name = parse_args(sys.argv[1:])

    path = ""
    if directories:
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)

    if file_name is None:
        return

    file_path = os.path.join(path, file_name)
    lines = read_content()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    already_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if already_exists:
            file.write("\n")
        file.write(timestamp + "\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


create_file()
