import os
from typing import List, Union
from pathlib import Path
from datetime import datetime
import argparse


def create_directory(path_components: List[str]) -> None:
    dir_path = os.path.join(*path_components)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory created: {dir_path}")


def create_file(filepath: Union[str, Path]) -> None:
    filepath = str(filepath)
    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    else:
        with open(filepath, "a") as file:
            file.write("\n")
            file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")

    print(f"File is ready: {filepath}")
    with open(filepath, "a") as file:
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1
    print(f"Content added to file: {filepath}")


def main(args: List[str]) -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and files.")
    parser.add_argument("-d", nargs="+",
                        help="Path components for the directory.")
    parser.add_argument("-f", help="File name to create.")

    parsed_args = parser.parse_args(args)

    if parsed_args.d:
        create_directory(parsed_args.d)

    if parsed_args.f:
        if parsed_args.d:
            file_path = os.path.join(*parsed_args.d, parsed_args.f)
        else:
            file_path = parsed_args.f
        create_file(file_path)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
