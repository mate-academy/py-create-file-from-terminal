import os
import argparse
from datetime import datetime
from typing import Any


def create_directory(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)


def create_file(directory: str, filename: str) -> None:
    file_path = os.path.join(directory, filename)

    with open(file_path, "a") as file:
        lines = []
        line_number = 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(f"{line_number} {line}")
            line_number += 1
        content = "\n".join(lines)
        file.write(timestamp + "\n" + content)


def parse_arguments() -> Any:
    parser = argparse.ArgumentParser(description="Create directory or file")
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file")
    return parser.parse_args()


def create_directory_and_file() -> None:
    args = parse_arguments()
    if args.directory:
        directory_path = os.path.join(*args.directory)
        create_directory(directory_path)
    if args.file:
        file_name = args.file
        create_file(".", file_name)


if __name__ == "__main__":
    create_directory_and_file()
