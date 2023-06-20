import sys
import os
from datetime import datetime


def get_content() -> list:
    content = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content.append(timestamp)
    line_number = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(f"{line_number} {line}")
        line_number += 1
    return content


def create_file(path: str) -> None:
    mode = "a" if os.path.exists(path) else "w"
    with open(path, mode) as file:
        for line in get_content():
            file.write(line + "\n")
        file.write("\n")


def create_directory(path: str) -> None:
    os.makedirs(path)


def parse_arguments() -> None:
    arguments = sys.argv[1:]
    directory_path = ""
    file_name = None

    if "-f" in arguments:
        index = arguments.index("-f")
        file_name = arguments[index + 1]
        arguments.remove("-f")
        arguments.remove(file_name)
    if "-d" in arguments:
        index = arguments.index("-d")
        directory_path = os.path.join(*arguments[index + 1:])

    if directory_path:
        create_directory(directory_path)
    if file_name:
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)


if __name__ in "__main__":
    parse_arguments()
