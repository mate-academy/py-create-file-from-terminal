import os
import argparse
from datetime import datetime
from typing import LiteralString

parser = argparse.ArgumentParser(description="Create a file in specified directory.")
parser.add_argument("-d", "--directory", nargs="+", required=False, help="Path to the directory: `-d dir1 dir2`.")
parser.add_argument("-f", "--file", required=False, help="Specify the filename to create.")
args = parser.parse_args()
directory_args = args.directory
filename = args.file


def create_path(directories: list) -> LiteralString | str | bytes:
    path = os.path.join(*directories)
    return path


def get_last_line_number(path: LiteralString | str | bytes) -> int:
    try:
        with open(path, "r") as input_file:
            lines = input_file.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0


if directory_args:
    dir_path = create_path(["./", *directory_args])
    os.makedirs(dir_path, exist_ok=True)

if filename:
    file_path = create_path(["./", *directory_args, filename])
    is_file_exists = os.path.exists(file_path)
    modifier = "a" if is_file_exists else "w"
    line_number = get_last_line_number(file_path) if is_file_exists else 0

    with open(file_path, modifier) as input_file:
        if not is_file_exists:
            date_time_now = datetime.now()
            input_file.write(date_time_now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        while True:
            next_line = input("Enter content: ")

            if next_line == "stop":
                break

            line_number += 1
            input_file.write(f"{line_number} {next_line}\n")
