import os
import sys
from datetime import datetime
from typing import Optional


def create_file(directory: Optional[str],
                filename: Optional[str],
                content: Optional[str]) -> None:
    filepath = get_filepath(directory, filename)
    initialize_file(filepath)
    input_content(filepath)


def get_filepath(directory: Optional[str], filename: Optional[str]) -> str:
    if directory:
        os.makedirs(directory, exist_ok=True)
        return os.path.join(directory, filename)
    else:
        return filename


def initialize_file(filepath: str) -> None:
    if os.path.isfile(filepath):
        with open(filepath, "a") as file:
            file.write("\n\n")
    else:
        with open(filepath, "w") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")


def input_content(filepath: str) -> None:
    line_number = 1
    while True:
        line = input(f"Enter content line {line_number}: ")
        if line.lower() == "stop":
            break
        with open(filepath, "a") as file:
            file.write(f"{line_number} {line}\n")
        line_number += 1


if __name__ == "__main__":
    args = sys.argv[1:]

    directory: Optional[str] = None
    filename: Optional[str] = None
    content: Optional[str] = None

    while args:
        arg = args.pop(0)
        if arg == "-d":
            directory = os.path.join(directory,
                                     args.pop(0))\
                if directory else args.pop(0)
        elif arg == "-f":
            filename = args.pop(0)
