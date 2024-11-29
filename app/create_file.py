import sys

import os
from datetime import datetime

import_arg = sys.argv


def create_file(path: str = "") -> None:
    file_name = os.path.join(path, import_arg[import_arg.index("-f") + 1])

    if not os.path.exists(file_name):
        new_file = open(file_name, "w")
        new_file.close()

    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1

        while (True):
            input_str = input("Enter content line:")

            if input_str == "stop":
                file.write("\n\n")
                break

            file.write(f"{line_number} {input_str} \n")
            line_number += 1


def create_dir() -> str:
    index_begin_path = import_arg.index("-d")

    if "-f" in import_arg:
        index_end_path = import_arg.index("-f")
        path = os.path.join(*import_arg[index_begin_path + 1: index_end_path])
    else:
        path = os.path.join(*import_arg[index_begin_path + 1:])

    if not os.path.exists(path):
        os.makedirs(path)

    return str(path)


if "-d" in import_arg and "-f" in import_arg:
    create_file(create_dir())
elif "-d" in import_arg:
    create_dir()
elif "-f" in import_arg:
    create_file()
