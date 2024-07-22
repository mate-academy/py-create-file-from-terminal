import os
import sys
from datetime import datetime
from typing import Union, LiteralString


def create_directory(directories: list[str]) -> Union[str, LiteralString]:
    path = os.getcwd()
    for directory in directories:
        path = os.path.join(path, directory)
    return path


def file_creator(file):
    with open(file, "a") as f:
        time_now = datetime.now()
        f.write(time_now.strftime("%m-%d-%Y %H:%M:%S + /n"))

        i = 1
        while True:
            content_line = input("Enter content line:")
            if content_line == "stop":
                break
            f.write(str(i) + ' ' + content_line + "/n")
            i += 1


def create_file() -> None:
    if "-f" in sys.argv and "-d" in sys.argv:
        directories = sys.argv[sys.argv.index('-d') + 1: sys.argv.index('-f')]
        file = sys.argv[sys.argv.index('-f') + 1]
        file_name = os.path.join(create_directory(directories), file)
        file_creator(file_name)
    elif "-f" in sys.argv:
        file = sys.argv[sys.argv.index('-f') + 1]
        file_creator(file)
    elif "-d" in sys.argv:
        directories = sys.argv[sys.argv.index('-d') + 1:]
        create_directory(directories)


if __name__ == "__main__":
    create_file()
