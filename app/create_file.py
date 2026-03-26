import os
import sys
from datetime import datetime


def get_directory_and_file_name(arguments: list[str]) -> tuple[list[str], str]:
    directory_parts = []
    file_name = ""

    if "-d" in arguments:
        dir_index = arguments.index("-d")
    elif "--dir" in arguments:
        dir_index = arguments.index("--dir")
    else:
        dir_index = -1

    if "-f" in arguments:
        file_index = arguments.index("-f")
    elif "--file" in arguments:
        file_index = arguments.index("--file")
    else:
        file_index = -1

    if file_index == -1 or file_index + 1 >= len(arguments):
        raise ValueError("File name is missing.")

    file_name = arguments[file_index + 1]

    if dir_index != -1:
        directory_parts = arguments[dir_index + 1:file_index]

    return directory_parts, file_name


def get_content_lines() -> list[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def build_content(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [timestamp]

    for index, line in enumerate(lines, start=1):
        content.append(f"{index} {line}")

    return "\n".join(content)


def write_to_file(file_path: str, content: str) -> None:
    file_exists = os.path.exists(file_path)
    has_content = file_exists and os.path.getsize(file_path) > 0

    with open(file_path, "a", encoding="utf-8") as file:
        if has_content:
            file.write("\n\n")
        file.write(content)
        file.write("\n")


def main() -> None:
    arguments = sys.argv[1:]
    directory_parts, file_name = get_directory_and_file_name(arguments)

    if directory_parts:
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = file_name

    lines = get_content_lines()
    content = build_content(lines)
    write_to_file(file_path, content)


if __name__ == "__main__":
    main()
