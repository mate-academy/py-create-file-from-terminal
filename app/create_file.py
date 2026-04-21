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
            continue

        if current_flag == "-f" and file_name is None:
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


def build_content_block(content_lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{line_number} {line}"
        for line_number, line in enumerate(content_lines, start=1)
    ]

    return "\n".join([timestamp, *numbered_lines])


def create_directory_path(directories: list[str]) -> str:
    if not directories:
        return ""

    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def write_file_content(file_path: str, content_lines: list[str]) -> None:
    content_block = build_content_block(content_lines)

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "a") as source_file:
            source_file.write("\n\n")
            source_file.write(content_block)
        return

    with open(file_path, "a") as source_file:
        source_file.write(content_block)


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])
    directory_path = create_directory_path(directories)

    if file_name is None:
        return

    file_path = os.path.join(directory_path, file_name) if directory_path else file_name
    content_lines = read_content_lines()
    write_file_content(file_path, content_lines)


main()
