import os
import sys
from datetime import datetime


def create_directory(args: list, file_name: str = "") -> None:
    directories = []
    for arg in args:
        if arg != "-f" and arg != file_name:
            directories.append(arg)
    path = os.path.join(*directories)
    os.makedirs(path)


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
            create_directory(args, file_name)
        create_file(file_name)
        return
    if "-d" in args:
        create_directory(args)
