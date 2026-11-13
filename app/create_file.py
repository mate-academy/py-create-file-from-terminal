import os
import sys
from datetime import datetime


def parse_arguments(arguments: list) -> tuple:
    directories = []
    file_name = None
    current_flag = None

    for argument in arguments:
        if argument in ("-d", "-f"):
            current_flag = argument
        elif current_flag == "-d":
            directories.append(argument)
        elif current_flag == "-f" and file_name is None:
            file_name = argument

    return directories, file_name


def read_content_lines() -> list:
    content_lines = []
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content_lines.append(content_line)
    return content_lines


def format_entry(content_lines: list) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{number} {content_line}"
        for number, content_line in enumerate(content_lines, 1)
    ]
    return "\n".join([timestamp] + numbered_lines) + "\n"


def create_file() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])

    directory_path = os.path.join(*directories) if directories else ""
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name:
        file_path = os.path.join(directory_path, file_name)
        separator = "\n" if os.path.exists(file_path) else ""

        with open(file_path, "a", encoding="utf-8") as target_file:
            target_file.write(separator + format_entry(read_content_lines()))


create_file()
