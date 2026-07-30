import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    directories = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")

            if d_index < f_index:
                directories = args[d_index + 1:f_index]
            else:
                directories = args[d_index + 1:]
        else:
            directories = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

        if "-d" in args:
            d_index = args.index("-d")

            if d_index < f_index:
                directories = args[d_index + 1:f_index]
            else:
                directories = args[d_index + 1:]

    if directories:
        os.makedirs(os.path.join(*directories), exist_ok=True)

    if file_name is None:
        return

    file_path = os.path.join(*directories, file_name)

    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


create_file()
