import os
import sys
from datetime import datetime


def get_content_lines() -> list[str]:
    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    return content_lines


def create_path(directory_parts: list[str]) -> str:
    if not directory_parts:
        return ""

    directory_path = directory_parts[0]

    for directory_name in directory_parts[1:]:
        directory_path = os.path.join(directory_path, directory_name)

    return directory_path


def get_file_name(arguments: list[str]) -> str:
    if "-f" not in arguments:
        return ""

    file_flag_index = arguments.index("-f")
    if file_flag_index + 1 >= len(arguments):
        return ""

    return arguments[file_flag_index + 1]


def get_directory_parts(arguments: list[str]) -> list[str]:
    if "-d" not in arguments:
        return []

    directory_flag_index = arguments.index("-d")

    if "-f" not in arguments:
        return arguments[directory_flag_index + 1:]

    file_flag_index = arguments.index("-f")

    if directory_flag_index < file_flag_index:
        return arguments[directory_flag_index + 1:file_flag_index]

    return arguments[directory_flag_index + 1:]


def build_content_block(content_lines: list[str]) -> str:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{line_number} {line}"
        for line_number, line in enumerate(content_lines, start=1)
    ]
    return "\n".join([current_time] + numbered_lines)


def write_to_file(file_path: str, content_block: str) -> None:
    file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a", encoding="utf-8") as source_file:
        if file_exists:
            source_file.write("\n\n")
        source_file.write(content_block)


def main() -> None:
    arguments = sys.argv[1:]
    directory_parts = get_directory_parts(arguments)
    file_name = get_file_name(arguments)
    directory_path = create_path(directory_parts)

    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if not file_name:
        return

    file_path = file_name

    if directory_path:
        file_path = os.path.join(directory_path, file_name)

    content_lines = get_content_lines()
    content_block = build_content_block(content_lines)
    write_to_file(file_path, content_block)


main()
