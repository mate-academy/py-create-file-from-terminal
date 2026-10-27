import os
import sys
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    dirs = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args and args.index("-f") > d_index:
            dirs = args[d_index + 1:args.index("-f")]
        else:
            dirs = args[d_index + 1:]

    if "-f" in args:
        file_name = args[args.index("-f") + 1]

    return dirs, file_name


def create_directories(dirs: list) -> str:
    path = ""
    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
    return path


def write_file_content(file_path: str) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for number, line in enumerate(lines, 1):
            file.write(f"{number} {line}\n")


def create_file() -> None:
    dirs, file_name = parse_arguments(sys.argv)
    path = create_directories(dirs)

    if file_name:
        write_file_content(os.path.join(path, file_name))


create_file()
