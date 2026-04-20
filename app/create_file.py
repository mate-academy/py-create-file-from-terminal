#!/usr/bin/env python3

import sys
import os
from datetime import datetime
from typing import List


def create_directories(directory_names: List[str]) -> str:
    if not directory_names:
        return "."

    path = os.path.join(*directory_names)
    os.makedirs(path, exist_ok=True)
    return path


def get_file_content() -> List[str]:
    content_lines = []
    line_number = 1

    while True:
        user_input = input("Enter content line: ")
        if user_input.lower() == "stop":
            break
        content_lines.append(f"{line_number} {user_input}")
        line_number += 1

    return content_lines


def format_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def write_file_content(file_path: str, content_lines: List[str]) -> None:
    timestamp = format_timestamp()

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode, encoding="utf-8") as file:
        if mode == "a":
            file.write("\n")

        file.write(f"{timestamp}\n")
        for line in content_lines:
            file.write(f"{line}\n")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(1)

    directories = []
    filename = None

    arg_index = 1
    while arg_index < len(sys.argv):
        if sys.argv[arg_index] == "-d":
            arg_index += 1
            while (arg_index < len(sys.argv) and not
                   sys.argv[arg_index].startswith("-")):
                directories.append(sys.argv[arg_index])
                arg_index += 1
        elif sys.argv[arg_index] == "-f":
            arg_index += 1
            if arg_index < len(sys.argv):
                filename = sys.argv[arg_index]
                arg_index += 1
        else:
            arg_index += 1

    target_path = create_directories(directories)

    if filename:
        file_path = os.path.join(target_path, filename)
        content_lines = get_file_content()
        write_file_content(file_path, content_lines)
    elif directories:
        pass
    else:
        pass


if __name__ == "__main__":
    main()
