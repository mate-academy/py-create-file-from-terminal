import sys
import os
from datetime import datetime


def create_directory(directory: list = None) -> None:
    if not directory:
        directory = [folder for folder in sys.argv[2:]]

    path = directory[0]
    if len(directory[1:]) > 1:
        for folder in directory[1:]:
            os.mkdir(path)
            path += "/" + folder
    os.mkdir(path)


def create_file(directory: str = None) -> None:
    if directory:
        path = directory
    else:
        path = sys.argv[2]

    if os.path.exists(path):
        mode = "a"
    else:
        mode = "w"

    with open(path, mode) as f:
        f.write(datetime.now().strftime("%y-%m-%d %H:%M:%S") + "\n")
        line = 1

        while True:
            content = input("Enter content line: ")
            if content.strip() == "stop":
                break
            f.write(f"{line} {content}\n")
            line += 1
        f.write("\n")


def create_directory_and_file() -> None:
    directory = [folder for folder in sys.argv[2: sys.argv.index("-f")]]

    create_directory(directory)

    directory = "/".join(directory)
    file_name = sys.argv[sys.argv.index("-f") + 1]
    path = os.path.join(directory, file_name)

    create_file(path)


if "-d" in sys.argv and "-f" not in sys.argv:
    create_directory()

if "-f" in sys.argv and "-d" not in sys.argv:
    create_file()

if "-d" in sys.argv and "-f" not in sys.argv:
    create_directory_and_file()
