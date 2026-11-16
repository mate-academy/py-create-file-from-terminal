import os
import sys
from datetime import datetime
from typing import TextIO

DIRECTORY_FLAG = "-d"
FILE_FLAG = "-f"
STOP_WORD = "stop"


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    directories = []
    file_names = []
    current_flag = None

    for argument in arguments:
        if argument in (DIRECTORY_FLAG, FILE_FLAG):
            current_flag = argument
        elif current_flag == DIRECTORY_FLAG:
            directories.append(argument)
        elif current_flag == FILE_FLAG:
            file_names.append(argument)

    file_name = file_names[0] if file_names else None
    return directories, file_name


def read_content_lines() -> list[str]:
    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line == STOP_WORD:
            break
        content_lines.append(line)

    return content_lines


def write_content(
    target_file: TextIO,
    content_lines: list[str],
    separator: str,
) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    target_file.write(f"{separator}{timestamp}\n")
    for line_number, line in enumerate(content_lines, start=1):
        target_file.write(f"{line_number} {line}\n")


def create_file() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])

    directory_path = ""
    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)

    if file_name is None:
        return

    file_path = os.path.join(directory_path, file_name)
    separator = "\n" if os.path.exists(file_path) else ""

    with open(file_path, "a") as target_file:
        content_lines = read_content_lines()
        write_content(target_file, content_lines, separator)


create_file()
