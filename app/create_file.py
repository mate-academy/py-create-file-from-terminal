import os
import datetime
from typing import TextIO
import argparse


def get_time() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def create_or_update_file(path_to_file: str) -> None:
    if not os.path.exists(path_to_file):
        with open(path_to_file, "w") as output_file:
            output_file.write(get_time() + "\n")
            write_content(output_file)
    else:
        with open(path_to_file, "a") as output_file:
            output_file.write(get_time() + "\n")
            write_content(output_file)


def write_content(output_file: TextIO) -> None:
    line_number = 1
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        output_file.write(f"{line_number} {content}\n")
        line_number += 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directories",
        nargs="+",
        help="List of directories to create")
    parser.add_argument(
        "-f",
        "--file",
        help="File name to create")
    args = parser.parse_args()
    print(args)

    if args.directories:
        dir_path = os.path.join(*args.directories)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = None

    file_path = os.path.join(dir_path, args.file) if dir_path else args.file

    create_or_update_file(file_path)


if __name__ == "__main__":
    main()
