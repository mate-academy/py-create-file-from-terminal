import os
from datetime import datetime
import argparse


def create_directory(directory_names: list) -> None:
    parent_dir = os.getcwd()
    for directory in directory_names:
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)


def create_file(name: str) -> None:
    with open(name, "w") as source_file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{date}\n")
        new_line = input("Enter content line: ")
        while new_line != "stop":
            source_file.write(f"{new_line}\n")
            new_line = input("Enter content line: ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--director", action="store_true")
    parser.add_argument(
        "name",
        nargs=argparse.ZERO_OR_MORE,
        help="names of directory"
    )
    parser.add_argument("-f", "--create", action="append")

    args = parser.parse_args()

    if args.director:
        create_directory(args.name)
    if args.create:
        create_file(args.create[0])
