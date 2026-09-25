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
            continue
        if current_flag == "-d":
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


def write_content(file_path: str, content_lines: list) -> None:
    is_existing_file = (
        os.path.isfile(file_path) and os.path.getsize(file_path) > 0
    )
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as target_file:
        if is_existing_file:
            target_file.write("\n")
        target_file.write(f"{timestamp}\n")
        for line_number, content_line in enumerate(content_lines, start=1):
            target_file.write(f"{line_number} {content_line}\n")


def create_file() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])

    directory_path = os.path.join(*directories) if directories else ""
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name is None:
        return

    file_path = os.path.join(directory_path, file_name)
    write_content(file_path, read_content_lines())


create_file()
