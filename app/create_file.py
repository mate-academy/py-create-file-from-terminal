import os
import sys
from datetime import datetime


def parse_args(args: list) -> tuple:
    directories = []
    filename = None
    flag = None

    for item in args:
        if item in ["-d", "-f"]:
            flag = item
        elif flag == "-d":
            directories.append(item)
        elif flag == "-f":
            filename = item

    return directories, filename


def create_directory(directories: list) -> None:
    path = os.path.join(*directories)
    os.makedirs(path)


def create_file(filename: str, directories: list | None = None) -> None:
    path = filename
    if directories:
        path = os.path.join(*directories, filename)

    with open(path, "a") as file:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            file.write("\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        i = 1
        while (content := input("Enter content line: ")) != "stop":
            file.write(f"{i} {content}\n")
            i += 1


if __name__ in {"__main__", "<run_path>"}:
    args = sys.argv[1:]
    directories, filename = parse_args(args)
    if directories:
        create_directory(directories)
    if filename:
        create_file(filename, directories)
