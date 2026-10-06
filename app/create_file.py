import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    directories = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        end = len(args)
        if "-f" in args and args.index("-f") > d_index:
            end = args.index("-f")
        directories = args[d_index + 1:end]

    if "-f" in args:
        file_name = args[args.index("-f") + 1]

    path = os.path.join(*directories) if directories else ""
    if directories:
        os.makedirs(path, exist_ok=True)

    if file_name is None:
        return

    file_path = os.path.join(path, file_name)

    lines = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    number = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{number} {line}")
        number += 1

    separator = "\n" if os.path.exists(file_path) else ""
    with open(file_path, "a") as file:
        file.write(separator + "\n".join(lines) + "\n")


create_file()
