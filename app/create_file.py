import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[2:]
    file_name = args[args.index("-f") + 1]
    content = input("Enter content line: ")
    current_dt = datetime.now()
    line_number = 1
    if "-d" and "-f" in args:
        directories = args
        directories.remove("-f")
        directories.remove(file_name)
        path = os.path.join(*directories)
        os.makedirs(path)
        with open(file_name, "a") as file:
            file.write(f"{current_dt}\n")
            while True:
                if content == "stop":
                    break
                file.write(f"{line_number}{content}\n")
    if "-d" in args:
        directories = sys.argv[(sys.argv.index("-d") + 1):]
        path = os.path.join(*directories)
        os.makedirs(path)
    if "-f" in args:
        with open(file_name, "a") as file:
            file.write(f"{current_dt}\n")
            while True:
                if content == "stop":
                    break
                file.write(f"{line_number}{content}\n")
