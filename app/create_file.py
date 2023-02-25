import os
import argparse
from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def write_to_file(file_name: str) -> None:
    with open(file_name, "a") as source_file:
        time_now = datetime.now()
        time_now_formatted = time_now.strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{time_now_formatted}\n")
        line_number = 1
        typing = True
        while typing:
            line = input("Enter content line: ")
            if line == "stop":
                break
            source_file.write(f"{line_number} {line}\n")

            line_number += 1


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directories", action="append", nargs="*")
    parser.add_argument("-f", "--file_name")
    args = parser.parse_args()
    if args.directories:
        path = create_path(*args.directories)
        if not os.path.exists(path):
            os.makedirs(path)
    if args.file_name:
        if path:
            path = create_path([path, args.file_name])
        else:
            path = args.file_name
        write_to_file(path)


if __name__ == "__main__":
    create_file()
