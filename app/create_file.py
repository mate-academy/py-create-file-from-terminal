import argparse
import os

from datetime import datetime


def get_args() -> list:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", help="Directory name", nargs="+")
    parser.add_argument("-f", "--file", help="File name")
    return parser.parse_args()


def get_path() -> str:
    args = get_args()
    path_file = args.file
    if args.dir:
        path_dir = ""
        for name in args.dir:
            path_dir += os.path.join(name + os.sep)
        path_file = os.path.join(path_dir, args.file)
        os.makedirs(path_dir, exist_ok=True)
    return path_file


def write_file() -> None:
    with open(get_path(), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{count} {line}\n")
            count += 1


write_file()
