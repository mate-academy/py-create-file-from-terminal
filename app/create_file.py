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
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        print("  -d: Create directories (each directory as separate argument)")
        print("  -f: Create file with specified name")
        sys.exit(1)

    directories = []
    filename = None

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            i += 1
            while i < len(sys.argv) and not sys.argv[i].startswith("-"):
                directories.append(sys.argv[i])
                i += 1
        elif sys.argv[i] == "-f":
            i += 1
            if i < len(sys.argv):
                filename = sys.argv[i]
                i += 1
        else:
            i += 1

    target_path = create_directories(directories)

    if filename:
        file_path = os.path.join(target_path, filename)
        print(f"Creating file: {file_path}")

        content_lines = get_file_content()
        write_file_content(file_path, content_lines)

        print(f"File '{filename}' created successfully in '{target_path}'")
    elif directories:
        print(f"Directories created successfully: {target_path}")
    else:
        print("No action specified. Use -d for directories or -f for file "
              "creation.")


if __name__ == "__main__":
    main()
