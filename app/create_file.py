import sys
import os
from datetime import datetime
from typing import List


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)


def get_existing_content(file_path: str) -> str:
    existing_content = ""
    if os.path.exists(file_path):
        with open(file_path, "r") as file_handle:
            existing_content = file_handle.read()
    return existing_content


def write_content_to_file(file_path: str, content: str) -> None:
    with open(file_path, "a") as file_handle:
        file_handle.write(content)


def create_file(directory: List[str], filename: str) -> None:
    directory_path = os.path.join(*directory)
    create_directory(directory_path)

    file_path = os.path.join(directory_path, filename)

    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    line_number = 1
    while True:
        line = input(f"Enter content line {line_number}: ")
        if line.lower() == "stop":
            break
        lines.append(f"{line_number} {line}")
        line_number += 1

    write_content_to_file(
        file_path,
        f"\n{current_timestamp}\n{''.join(lines)}\n"
    )


if __name__ == "__main__":
    if "-d" in sys.argv:
        index_d = sys.argv.index("-d")
        directory = sys.argv[index_d + 1:]
        filename = "file.txt"
        create_file(directory, filename)
    elif "-f" in sys.argv:
        index_f = sys.argv.index("-f")
        directory = []
        filename = sys.argv[index_f + 1]
        create_file(directory, filename)
    else:
        print("Usage: python create_file.py -d <directory> OR -f <filename>")
