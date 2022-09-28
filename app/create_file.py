from datetime import datetime
import os
import sys


def create_from_terminal() -> None:
    file = sys.argv
    create_file = False
    create_dir = False

    for flag in file:
        if flag == "-d":
            create_dir = True
        if flag == "-f":
            create_file = True

    if create_dir and not create_file:
        ind = file.index("-d")
        os.makedirs("/".join(file[ind + 1:]))

    if create_dir and create_file:
        ind_dir = file.index("-d")
        ind_file = file.index("-f")
        name = file[ind_file + 1]
        path = file[ind_dir + 1: ind_file]
        create_new_file(name, path)

    if create_file and not create_dir:
        ind_file = file.index("-f")
        name = file[ind_file + 1]
        create_new_file(name)


def create_new_file(name: str, path: list = None):
    if path:
        os.makedirs("/".join(path))
        name = "/".join(path) + "/" + name

    with open(name, "w") as new_file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(f"{time}\n")
        line_number = 1
        content_line = input("Enter content line: ")
        while content_line != "stop":
            new_file.write(f"{line_number} "
                           f"Line{line_number} {content_line} \n")
            content_line = input("Enter content line: ")
            line_number += 1
