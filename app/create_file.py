import os
import argparse
from datetime import datetime
from typing import TextIO


def create_path(directories: list, file_name: str = "") -> str:
    path = os.path.join(*directories, file_name)
    return path


def handle_user_input(out_file: TextIO) -> None:
    out_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    counter = 0
    while True:
        counter += 1
        in_text = input("Enter content line: ")
        if in_text.strip().lower() == "stop":
            out_file.write("\n")
            break
        out_file.write(f"{counter} {in_text}\n")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", type=str,
                    help="Output file name")
parser.add_argument("-d", "--directory", nargs="+", type=str,
                    help="Directory path")

args = parser.parse_args()

if args.directory:
    dir_path = create_path(args.directory)
    os.makedirs(dir_path, exist_ok=True)
else:
    dir_path = ""

if args.file:
    file_path = args.file
    with open(create_path([dir_path], file_path), "a") as file:
        handle_user_input(file)
