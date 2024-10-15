import os

import sys

from datetime import datetime

from typing import TextIO


def create_file_with_content(file_path: str) -> None:
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file_handle:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_handle.write(f"{timestamp}\n")

        write_content_to_file(file_handle, starting_line_number=1)


def write_content_to_file(
        file_handle: TextIO,
        starting_line_number: int
) -> None:
    line_number = starting_line_number
    while True:
        content = input("Enter content line: ")
        if content.strip().lower() == "stop":
            break
        file_handle.write(f"{line_number} {content}\n")
        line_number += 1


def create_directory(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory '{dir_path}' created.")


def handle_file_creation(dir_path: str, file_name: str) -> None:
    create_directory(dir_path)
    file_path = os.path.join(dir_path, file_name)
    create_file_with_content(file_path)


def create_file_in_current_directory(file_name: str) -> None:
    file_path = os.path.join(os.getcwd(), file_name)
    create_file_with_content(file_path)


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1

        dir_path = os.path.join(*sys.argv[dir_index:file_index - 1])
        file_name = sys.argv[file_index]

        handle_file_creation(dir_path, file_name)

    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        dir_path = os.path.join(*sys.argv[dir_index:])
        create_directory(dir_path)

    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]

        create_file_in_current_directory(file_name)

    else:
        print(
            "Invalid arguments. Use -d for directory and -f for file creation."
        )
