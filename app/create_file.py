from sys import argv
from os import makedirs, path
from datetime import datetime


def find_dir() -> str:
    d_index = argv.index("-d")
    if "-f" in argv:
        f_index = argv.index("-f")
        directory = "/".join(argv[d_index + 1: f_index]) + "/"
    else:
        directory = "/".join(argv[d_index + 1:]) + "/"

    if not path.exists(directory):
        makedirs(directory)

    return path.join(directory)


def find_name() -> str:
    f_index = argv.index("-f")
    name = argv[f_index + 1]
    return name


def write_content(file_path: str) -> None:
    with open(file_path, "w") as f:
        f.write(datetime.now().strftime("%Y/%m/%d, %H:%M:%S") + "\n")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(line + "\n")


def create_file() -> None:
    if "-f" not in argv:
        find_dir()
    if "-d" not in argv:
        file_name = find_name()
        write_content(file_name)
    if "-d" in argv and "-f" in argv:
        file_name = find_name()
        file_path = find_dir()
        write_content(file_path + file_name)


create_file()
