import os
import sys
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
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


def read_content_lines() -> list[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_content(file_path: str, content_lines: list[str]) -> None:
    file_has_content = (
        os.path.isfile(file_path) and os.path.getsize(file_path) > 0
    )
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as target_file:
        if file_has_content:
            target_file.write("\n")
        target_file.write(f"{timestamp}\n")
        for line_number, line in enumerate(content_lines, start=1):
            target_file.write(f"{line_number} {line}\n")


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
