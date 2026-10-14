import os
import sys
from datetime import datetime


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    dirs = []
    file_name = None
    current_flag = None

    for arg in args:
        if arg in ("-d", "-f"):
            current_flag = arg
        elif current_flag == "-d":
            dirs.append(arg)
        elif current_flag == "-f" and file_name is None:
            file_name = arg

    return dirs, file_name


def get_content_lines() -> list[str]:
    lines = []
    line_number = 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{line_number} {line}")
        line_number += 1

    return lines


def create_file() -> None:
    dirs, file_name = parse_args(sys.argv[1:])

    directory = os.path.join(*dirs) if dirs else ""
    if directory:
        os.makedirs(directory, exist_ok=True)

    if file_name is None:
        return

    file_path = os.path.join(directory, file_name)
    lines = get_content_lines()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    has_content = os.path.isfile(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a") as file:
        if has_content:
            file.write("\n")
        file.write(timestamp + "\n")
        for line in lines:
            file.write(line + "\n")


create_file()
