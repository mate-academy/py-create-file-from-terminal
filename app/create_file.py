import os
import sys
from datetime import datetime
from typing import List, Optional, Tuple


def parse_arguments(
    arguments: List[str],
) -> Tuple[Optional[str], Optional[str]]:

    if "-d" in arguments and "-f" in arguments:
        d_index = arguments.index("-d")
        f_index = arguments.index("-f")

        if d_index < f_index:
            directory_parts = arguments[d_index + 1:f_index]
            file_parts = arguments[f_index + 1:]
        else:
            file_parts = arguments[f_index + 1:d_index]
            directory_parts = arguments[d_index + 1:]

        if directory_parts:
            directory_path = os.path.join(*directory_parts)

        if file_parts:
            file_name = file_parts[0]

    elif "-d" in arguments:
        d_index = arguments.index("-d")
        directory_parts = arguments[d_index + 1:]

        if directory_parts:
            directory_path = os.path.join(*directory_parts)

    elif "-f" in arguments:
        f_index = arguments.index("-f")
        file_parts = arguments[f_index + 1:]

        if file_parts:
            file_name = file_parts[0]

    return directory_path, file_name


def read_content_lines() -> List[str]:
    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    return content_lines


def build_file_content(content_lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{index} {line}" for index, line in enumerate(content_lines, start=1)
    ]
    return timestamp + "\n" + "\n".join(numbered_lines)


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)


def write_file(file_path: str, content_lines: List[str]) -> None:
    new_content = build_file_content(content_lines)

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n\n" + new_content)
    else:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(new_content)


def main() -> None:
    arguments = sys.argv[1:]
    directory_path, file_name = parse_arguments(arguments)

    if directory_path:
        create_directory(directory_path)

    if file_name:
        content_lines = read_content_lines()

        if directory_path:
            file_path = os.path.join(directory_path, file_name)
        else:
            file_path = file_name

        write_file(file_path, content_lines)


if __name__ == "__main__":
    main()
