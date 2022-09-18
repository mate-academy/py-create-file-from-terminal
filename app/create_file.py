from sys import argv
from os import makedirs
from datetime import datetime


def make_dir(paths: list):
    try:
        d_index = paths.index("-d")
    except ValueError:
        return
    try:
        f_index = paths.index("-f")
    except ValueError:
        f_index = len(paths)
    try:
        makedirs("/".join(paths[d_index + 1:f_index]))
    except FileExistsError:
        return


def create_file(paths: list):
    try:
        f_index = paths.index("-f")
    except ValueError:
        return
    if f_index == len(paths) - 1:
        return
    if "-d" in paths:
        d_index = paths.index("-d")
        file_name = f"{'/'.join(paths[d_index + 1:f_index])}/{paths[-1]}"
    else:
        file_name = paths[-1]
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"{new_line}\n")
        file.write("\n")


make_dir(argv)
create_file(argv)
