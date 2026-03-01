import argparse
import os

from datetime import datetime
from typing import TextIO


def get_date_and_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_or_update_file(file_path: str) -> None:
    with open(file_path, "a+") as output_file:
        is_empty = output_file.tell() == 0

        if not is_empty:
            output_file.write("\n")

        output_file.write(get_date_and_time() + "\n")
        insert_content(output_file)


def insert_content(output_file: TextIO) -> None:
    line_number = 1

    while True:
        content_input = input("Enter the line content: ")
        if content_input == "stop":
            break
        output_file.write(f"{line_number} {content_input}\n")
        line_number += 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a file")
    parser.add_argument(
        "-d",
        "--dir",
        nargs="+",
        help="List of directories to create",
    )
    parser.add_argument(
        "-f",
        "--file",
        help="File name to create"
    )
    args = parser.parse_args()

    dir_path = str(os.path.join(*args.dir)) if args.dir else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, args.file)
    create_or_update_file(file_path)


if __name__ == "__main__":
    main()
