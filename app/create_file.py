import os
import sys
from datetime import datetime


def parse_arguments(arguments: list) -> tuple:
    directories: list = []
    filename: str | None = None

    index = 1
    while index < len(arguments):
        if arguments[index] == "-d":
            index += 1
            while (
                index < len(arguments)
                and not arguments[index].startswith("-")
            ):
                directories.append(arguments[index])
                index += 1
        elif arguments[index] == "-f":
            index += 1
            if index < len(arguments):
                filename = arguments[index]
                index += 1
        else:
            index += 1

    return directories, filename


def create_directories(directories: list) -> str:
    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def collect_content_lines() -> list:
    content_lines: list = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_content_to_file(file_path: str, content_lines: list) -> None:
    file_exists = os.path.isfile(file_path) and os.path.getsize(file_path) > 0
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as source_file:
        if file_exists:
            source_file.write("\n")
        source_file.write(f"{timestamp}\n")
        for line_number, line in enumerate(content_lines, start=1):
            source_file.write(f"{line_number} {line}\n")


directories, filename = parse_arguments(sys.argv)

directory_path = ""
if directories:
    directory_path = create_directories(directories)

if filename is not None:
    content_lines = collect_content_lines()
    if directory_path:
        file_path = os.path.join(directory_path, filename)
    else:
        file_path = filename
    write_content_to_file(file_path, content_lines)
