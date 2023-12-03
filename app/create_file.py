import os

import argparse

from datetime import datetime
from typing import Any


def create_directory(path_parts: str) -> Any:
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def create_file(file_name: str) -> None:

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, "a") as f:
        f.write("\n" + (str(current_time) + "\n"))
    with open(file_name, "a") as f:
        line_number = 1
        while True:
            content = input(str(f"Enter content line: {line_number} "))
            if content == "stop":
                break
            f.write(f"{line_number } Line{line_number} "
                    + "".join(content) + "\n")
            line_number += 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--filename")
    args = parser.parse_args()
    directory_path = ""
    if args.directory:
        directory_path = create_directory(args.directory)
    if args.filename:
        filename = os.path.join(directory_path, args.filename)
        create_file(filename)


if __name__ == "__main__":
    main()
