import os
import sys
from datetime import datetime


def parse_arguments(arguments: list) -> tuple:
    directory_parts = []
    file_name = None
    current_flag = None
    for argument in arguments:
        if argument in ("-d", "-f"):
            current_flag = argument
        elif current_flag == "-d":
            directory_parts.append(argument)
        elif current_flag == "-f" and file_name is None:
            file_name = argument
    return directory_parts, file_name


def read_content_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            return lines
        lines.append(line)


def write_content(file_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{number} {line}" for number, line in enumerate(lines, start=1)
    ]
    entry = "\n".join([timestamp] + numbered_lines) + "\n"
    file_has_content = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )
    with open(file_path, "a") as output_file:
        if file_has_content:
            output_file.write("\n")
        output_file.write(entry)


def create_file() -> None:
    directory_parts, file_name = parse_arguments(sys.argv[1:])
    directory = os.path.join(*directory_parts) if directory_parts else ""
    if directory:
        os.makedirs(directory, exist_ok=True)
    if file_name:
        write_content(os.path.join(directory, file_name), read_content_lines())


create_file()
