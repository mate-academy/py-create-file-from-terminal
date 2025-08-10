import os
import datetime
import argparse

from typing import Union


def create_file(file_name: str) -> None:

    is_new_file = not os.path.exists(file_name)

    with open(file_name, "a") as source_file:

        if not is_new_file:
            source_file.write("\n")

        line_count = 0
        source_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        while True:
            input_line = input("Enter content line:")

            if input_line == "stop":
                break

            line_count += 1
            source_file.write(f"{line_count} {input_line}\n")


def create_directory(path: Union[str, bytes]) -> None:

    if not os.path.exists(path):
        os.makedirs(path)

    os.chdir(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        type=str,
        nargs="+",
        help="List of directory"
    )
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="File"
    )

    args = parser.parse_args()
    if args.directory:
        create_directory(os.path.join(*args.directory))

    if args.file:
        create_file(args.file)
