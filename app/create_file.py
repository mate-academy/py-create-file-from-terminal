import datetime
import os
import sys


def create_file(path: str) -> None:
    path = os.path.join("app", path)
    with open(path, "a") as file:
        file.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                   + "\n")
        line = input("Enter content line: ")
        index = 1
        while line != "stop":
            file.write(f"{index} {line}\n")
            index += 1
            line = input("Enter content line: ")
        file.write("\n")


def create_dirs(dirs: list) -> None:
    for directory in dirs:
        os.makedirs(os.path.join("app", directory))


def read_line() -> None:
    line_args = sys.argv
    if "-d" in line_args:
        dirs = []
        for directory in line_args[line_args.index("-d") + 1:]:
            if directory != "-f":
                dirs.append(directory)
            else:
                break
        create_dirs(dirs)
    if "-f" in line_args:
        create_file(line_args[line_args.index("-f") + 1])


read_line()
