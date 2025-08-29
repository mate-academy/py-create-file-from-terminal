import sys
import os
import datetime
from typing import TextIO


def parse_args(args: list) -> list:
    path = []
    file_name = ""
    if ("-f" in args
        and args.index("-f") != -1
            and args[args.index("-f") + 1] != "-d"):
        file_name = args[args.index("-f") + 1]
    if ("-d" in args
        and args.index("-d") != -1
            and args[args.index("-d") + 1] != "-f"):
        for directory in args[args.index("-d") + 1:]:
            if directory == "-f":
                break
            else:
                path.append(directory)
    return [file_name, path]


def write_text(opened_file: TextIO) -> None:
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    index = 1
    opened_file.write(time)
    text = input("Enter content line: ")
    while text != "stop":
        text = str(index) + " " + text + "\n"
        index += 1
        opened_file.write(text)
        text = input("Enter content line: ")
    opened_file.write("\n")


def create_file() -> None:
    args = sys.argv
    filename_path = parse_args(args=args)
    if "-d" in args and "-f" not in args:
        os.makedirs(os.path.join(*filename_path[1]), exist_ok=True)
    if "-d" not in args and "-f" in args:
        with open(filename_path[0], "a", encoding="utf-8") as f:
            write_text(f)
    if "-d" in args and "-f" in args:
        path = os.path.join(*filename_path[1])
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, filename_path[0]),
                  "a", encoding="utf-8") as f:
            write_text(f)


create_file()
