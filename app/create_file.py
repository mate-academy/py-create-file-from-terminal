import sys
import os
from datetime import datetime
from typing import List


def create_directory(directory: List[str]) -> str:
    full_path = os.path.join(*directory)
    os.makedirs(full_path, exist_ok=True)
    return full_path


def get_existing_content(file_path: str) -> str:
    existing_content = ""
    if os.path.exists(file_path):
        with open(file_path, "r") as file_handle:
            existing_content = file_handle.read()
    return existing_content


def write_content_to_file(file_path: str, content: str) -> None:
    with open(file_path, "w") as file_handle:
        file_handle.write(content)


def create_file(directory: List[str], filename: str) -> None:
    full_path = create_directory(directory)
    file_path = os.path.join(full_path, filename)

    existing_content = get_existing_content(file_path)

    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    write_content_to_file(
        file_path,
        f"{current_timestamp}\n{existing_content}{''.join(lines)}"
    )


if __name__ == "__main__":
    if "-d" in sys.argv and "-f" in sys.argv:
        index_d = sys.argv.index("-d")
        index_f = sys.argv.index("-f")

        directory = sys.argv[index_d + 1:index_f]
        filename = sys.argv[index_f + 1]

        # Call the function with descriptive names
        create_file(directory, filename)
    else:
        print("Usage: python create_file.py -d <directory> -f <filename>")
