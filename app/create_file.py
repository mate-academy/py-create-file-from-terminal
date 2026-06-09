import argparse
import os
from datetime import datetime
from typing import LiteralString


def make_dirs(*args) -> LiteralString | str | bytes:
    path = os.path.join(*args)
    os.makedirs(path, exist_ok=True)
    return path


def make_file(name: LiteralString | str | bytes) -> None:
    file_exists = os.path.exists(name)
    with open(name, "a") as file:
        if file_exists:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def parse_args() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file")

    parsed_args = parser.parse_args()

    path = ""
    if parsed_args.directory:
        path = make_dirs(*parsed_args.directory)
    if parsed_args.file:
        make_file(os.path.join(str(path), parsed_args.file))


parse_args()
