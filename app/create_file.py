import os
import sys
from datetime import datetime


def write_input(path: str) -> None:
    line = input("Enter content line: ")
    if line == "stop":
        return
    number_of_line = 1
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as f:
        if os.path.getsize(path) > 0:
            f.write("\n")
        f.write(now_str + "\n")
        while line != "stop":
            f.write(f"{number_of_line} {line}\n")
            number_of_line += 1
            line = input("Enter content line: ")


def create_file() -> None:
    args = sys.argv[1:]
    if not args:
        return
    directory = []
    file_txt = None

    if "-f" in args:
        f_position = args.index("-f")
        if f_position + 1 >= len(args):
            print("No file specified")
            return
        file_txt = args[f_position + 1]

    if "-d" in args:
        d_position = args.index("-d")
        if "-f" in args:
            f_position = args.index("-f")
            if d_position < f_position:
                directory = args[d_position + 1: f_position]
            else:
                directory = args[d_position + 1:]
        else:
            directory = args[d_position + 1:]

    directory_path = None
    if directory:
        directory_path = os.path.join(*directory)
        os.makedirs(directory_path, exist_ok=True)

    if file_txt:
        if directory_path:
            path = os.path.join(directory_path, file_txt)
        else:
            path = file_txt
        write_input(path)


create_file()
