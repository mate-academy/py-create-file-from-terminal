import os
import argparse
from typing import TextIO
from datetime import datetime


def get_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def create_file(path: str) -> None:
    if not os.path.exists(path):
        with open(path, "w") as output_file:
            output_file.write(get_time() + "\n")
            write_content(output_file)
    else:
        with open(path, "a") as output_file:
            output_file.write("\n" + get_time() + "\n")
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
    parser.add_argument("-d",
                        "--directories", nargs="+",
                        help="List of directories to create")
    parser.add_argument("-f", "--file", help="File name to create")

    args = parser.parse_args()

    if args.directories:
        dir_path = os.path.join(*args.directories)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = None

    if args.file:
        file_path = os.path.join(dir_path,
                                 args.file) if dir_path else args.file
        create_file(file_path)


if __name__ == "__main__":
    main()
