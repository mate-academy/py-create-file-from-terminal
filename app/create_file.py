import os
import sys
from typing import TextIO


def fill_the_file(current_file: TextIO) -> None:
    import datetime
    current_file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    while True:
        current_input = input("Enter content line: ")
        if current_input == "stop":
            break
        current_file.write("\n" + current_input)


def create_file(directorys: str, file_name: str) -> None:
    current_directory = ""
    for directory in directorys.split(os.sep):
        current_directory = os.path.join(current_directory, directory)
        if os.path.exists(current_directory):
            continue
        os.mkdir(current_directory)
    if file_name:
        path = os.path.join(current_directory, file_name)
        with open(path, "w"):
            with open(path, "a") as current_file:
                fill_the_file(current_file)


def main() -> None:
    args = sys.argv[1:]
    directorys = [""]
    file_name = ""

    if "-f" in args:
        i = args.index("-f")
        file_name = args[i + 1]
        args = args[:i]

    if "-d" in args:
        i = args.index("-d")
        for directory_name in args[i + 1:]:
            directorys.append(directory_name)
    directorys = os.path.join(*directorys)

    create_file(directorys, file_name)


if __name__ == "__main__":
    main()
