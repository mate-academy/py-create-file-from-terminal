import sys

import os

from datetime import datetime


arguments = sys.argv


def make_directories(directories_path: list[str]) -> None:
    direct = ""
    for di in directories_path:
        direct += di
    os.makedirs(direct, exist_ok=True)


def create_file(path_name: str) -> None:
    with open(path_name, "a") as f:
        f.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S \n")))
        data = input("Enter content line: ")
        count = 0
        while data != "stop":
            count += 1
            f.write(f"{count} {data} \n")
            data = input("Enter content line: ")


if "-d" in arguments and "-f" in arguments:
    d_flag_index = arguments.index("-d")
    f_flag_index = arguments.index("-f")
    if f_flag_index > d_flag_index:
        directories = arguments[2:-2]
        file_name = arguments[-1]
    else:
        directories = arguments[d_flag_index + 1:]
        file_name = arguments[2]

    make_directories(directories)
    joined_path = os.path.join(*directories, file_name)
    create_file(joined_path)


elif "-d" in arguments:
    directories = arguments[2:]
    make_directories(directories)

elif "-f" in arguments:
    file_name = arguments[-1]
    create_file(file_name)
