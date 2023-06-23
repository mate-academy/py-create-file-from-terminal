import argparse
import os
import sys
from datetime import datetime
from typing import List


def create_file(file_path: str, filename: str, content: List[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(timestamp + "\n")
        for line in content:
            file.write(line + "\n")
        file.write("\n")

    print(f"File '{filename}' created successfully at '{file_path}'.")


def process_arguments() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directories", nargs="+", help="creates directory")
    parser.add_argument("-f", "--filename", help="creates file")
    arguments = parser.parse_args()

    filename = arguments.filename
    directories = "/".join(arguments.directories if arguments.directories else os.getcwd())
    os.makedirs(directories, exist_ok=True)
    file_path = os.path.join(directories, filename)

    if filename:
        content = get_content_from_input()
        create_file(file_path, filename, content)


def get_content_from_input() -> List[str]:
    content = []
    line = input("Enter content line: ")
    while line != "stop":
        content.append(line)
        line = input("Enter content line: ")
    return content


if __name__ == "__main__":
    process_arguments()
