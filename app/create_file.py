from sys import argv
import os
from datetime import datetime


def create_file(argv: list) -> None:
    f_appeared = False
    d_appeared = False
    index_f_appeared = 1
    while index_f_appeared < len(argv):
        if argv[index_f_appeared] == "-f":
            f_appeared = True
            file_path = argv[index_f_appeared + 1]
            index_f_appeared += 2
        else:
            d_appeared = True
            index_d_appeared = index_f_appeared + 1
            while index_d_appeared < len(argv) \
                    and argv[index_d_appeared] != "-f":
                index_d_appeared += 1
            folders = os.path.join(
                *argv[index_f_appeared + 1:index_d_appeared]
            )
            index_f_appeared = index_d_appeared
    if d_appeared:
        os.makedirs(folders, exist_ok=True)
    if f_appeared:
        if d_appeared:
            file_path = os.path.join(folders, file_path)
        file_existed = os.path.isfile(file_path)
        with open(file_path, "a") as file:
            if file_existed:
                print(file=file)
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=file)
            index_f_appeared = 1
            row = input("Enter content line: ")
            while row != "stop":
                print(index_f_appeared, row, file=file)
                index_f_appeared += 1
                row = input("Enter content line: ")


create_file(argv)
