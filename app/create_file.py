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
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    return content_lines


def build_entry(content_lines: list) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{line_number} {line}"
        for line_number, line in enumerate(content_lines, start=1)
    ]
    return "\n".join([timestamp, *numbered_lines]) + "\n"


def write_entry(file_path: str, entry: str) -> None:
    file_has_content = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a") as target_file:
        if file_has_content:
            target_file.write("\n")
        target_file.write(entry)


def create_file() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])

    directory_path = os.path.join(*directories) if directories else ""
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name is None:
        return

    content_lines = read_content_lines()
    file_path = os.path.join(directory_path, file_name)
    write_entry(file_path, build_entry(content_lines))


create_file()
