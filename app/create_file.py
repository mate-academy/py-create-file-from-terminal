import os
import sys
from datetime import datetime


def define_path(args: list) -> str:
    if "-d" in args:
        if "-f" in args:
            return os.path.join(*args[args.index("-d") + 1:args.index("-f")])
        return os.path.join(*args[args.index("-d") + 1:])


def define_file_name(args: list, path: str) -> str:
    if path:
        return os.path.join(path, args[-1])
    return args[-1]


def write_file(file_name: str) -> None:
    with open(file_name, "a") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line = input("Enter content line: ")
        page_number = 1
        while True:
            new_file.write(f"{page_number} {line}\n")
            page_number += 1
            line = input("Enter content line: ")
            if line == "stop":
                new_file.write("\n")
                break


def create_file_from_terminal(argv: list) -> None:
    path = define_path(argv)
    if path:
        os.makedirs(path, exist_ok=True)
    if "-f" in argv:
        file_name = define_file_name(argv, path)
        write_file(file_name)


arg_list = sys.argv
create_file_from_terminal(arg_list)
