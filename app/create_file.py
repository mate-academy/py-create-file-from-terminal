import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv
    directory = []
    filename = ""
    if "-d" in args:
        d_index = args.index("-d")
        for element in args[d_index + 1:]:
            if element == "-f":
                break
            directory.append(element)

    if "-f" in args:
        f_index = args.index("-f")
        filename = args[f_index + 1]

    dir_path = ""
    if directory:
        dir_path = os.path.join(*directory)
        os.makedirs(dir_path, exist_ok=True)

    filepath = os.path.join(dir_path, filename)

    lines = []
    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as f:
        f.write(f"\n{timestamp}\n")
        for i, text in enumerate(lines, start=1):
            f.write(f"{i} {text}\n")
