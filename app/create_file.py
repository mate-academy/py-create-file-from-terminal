import os
import sys
from datetime import datetime


def parse_arguments() -> tuple:
    if "-f" not in sys.argv:
        d_index = sys.argv.index("-d")
        directories = sys.argv[d_index + 1:]
        filename = None
        return directories, filename
    f_index = sys.argv.index("-f")
    filename = sys.argv[f_index + 1]
    if "-d" not in sys.argv:
        directories = []
    else:
        d_index = sys.argv.index("-d")
        if d_index < f_index:
            directories = sys.argv[d_index + 1:f_index]
        else:
            directories = sys.argv[d_index + 1:]
    return directories, filename


def create_path(directories: list, filename: str) -> str:
    path = os.path.join(*directories, filename)
    return path


def create_directories(directories: list) -> None:
    if directories:
        os.makedirs(os.path.join(*directories), exist_ok=True)


def get_content() -> list:
    content = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)
    return content


def create_file(path: str, content: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(path)
    with open(path, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for num, line in enumerate(content, start=1):
            file.write(f"{num} {line}\n")


def main() -> None:
    directories, filename = parse_arguments()
    create_directories(directories)
    if filename is None:
        return
    path = create_path(directories, filename)
    content = get_content()
    create_file(path, content)


main()
