from sys import argv
from os import makedirs
import os
from datetime import datetime


def create_file() -> None:
    args = argv
    path_parts = []
    file_name = None
    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            path_parts = args[d_index + 1: f_index]
        else:
            path_parts = args[d_index + 1:]
        if path_parts:
            path = os.path.join(*path_parts)
            makedirs(path, exist_ok=True)
    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        if path_parts:
            full_path = os.path.join(*path_parts, file_name)
        else:
            full_path = file_name
    else:
        full_path = None

    if full_path is not None:
        if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
            with open(full_path, "a") as a:
                a.write("\n")
        with open(full_path, "a") as f:
            number = 1
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(timestamp + "\n")
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                f.write(f"{number} {line}\n")
                number += 1


if __name__ == "__main__":
    create_file()
