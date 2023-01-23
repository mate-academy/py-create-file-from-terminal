import os
import sys
from datetime import datetime


def create_directory(args: list) -> None:
    str_ = " ".join(args)
    if str_.startswith("-f") or "-f" not in args:
        os.makedirs(os.path.join(*args[args.index("-d"):]))
        return
    os.makedirs(os.path.join(*args[args.index("-d"):args.index("-f")]))


def create_file(file_name: str) -> None:
    current_dt = datetime.now()
    with open(file_name, "a") as file:
        file.write(f"{current_dt}\n")
        content = input("Enter content line: ")
        line_number = 1
        while True:
            if content == "stop":
                break
            file.write(f"{line_number}{content}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[2:]
    if "-f" in args:
        file_name = args[args.index("-f") + 1]
        if "-d" in args:
            create_directory(args)
        create_file(file_name)
        return
    if "-d" in args:
        create_directory(args)
