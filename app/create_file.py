import sys
import os
import datetime
from typing import Any


def make_directory(name_dir: str) -> Any:
    os.makedirs(name_dir, exist_ok=True)
    return name_dir


def create_file(name_file: str) -> Any:
    content = []
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        line = input("Enter content line:")
        if line.lower() == "stop":
            break
        content.append(line)

    with open(name_file, "a") as exist_file:
        exist_file.write(f"{data}\n")
        for i, line in enumerate(content):
            exist_file.write(f"{i + 1} {line} \n")
        exist_file.write("\n")


def parse_arguments(args):
    if "-f" in args and "-d" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        if d_index < f_index:
            dir_path = make_directory(os.path.join(*args[d_index + 1:f_index]))
            file_path = os.path.join(dir_path, args[-1])
        else:
            dir_path = make_directory(os.path.join(*args[f_index + 1:]))
            file_path = os.path.join(dir_path, args[d_index + 1])

        create_file(file_path)
    elif "-f" in args:
        create_file(args[-1])
    elif "-d" in args:
        make_directory(os.path.join(*args[args.index("-d") + 1:]))
    else:
        print("Invalid arguments. Please provide '-d' for directory or '-f' for file.")


def main():
    args = sys.argv[1:]
    print(args)
    parse_arguments(args)
