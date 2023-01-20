import sys
import os
from datetime import datetime


args = sys.argv


def create_dirs(path_name: str) -> None:
    if not os.path.exists(path_name):
        os.makedirs(path_name)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file_out:
        line_number = 1
        print(datetime.strftime(datetime.now(), "%y-%m-%d %H:%M:%S"),
              file=file_out)
        while True:
            word = input("Enter content line: ")
            if word == "stop":
                break
            print(line_number, word, file=file_out)
            line_number += 1


if __name__ == "__main__": 
    current_dir = os.getcwd()
    if "-d" in args:
        if "-f" in args:
            new_dirs = args[args.index("-d"): -2]
            path = os.path.join(current_dir, *new_dirs)
            create_dirs(path)
        else:
            new_dirs = args[args.index("-d"):]
            path = os.path.join(current_dir, *new_dirs)
            create_dirs(path)
    if "-f" in args:
        create_file(args[-1])
