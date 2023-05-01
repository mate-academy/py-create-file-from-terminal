from sys import argv
import os
from datetime import datetime


def create_file(argv: list) -> None:
    f_appeared = "-f" in argv
    d_appeared = "-d" in argv
    if f_appeared:
        f_flag_index = argv.index("-f")
        file_path = argv[f_flag_index + 1]
    if d_appeared:
        d_flag_index = argv.index("-d")
        if f_appeared and d_flag_index < f_flag_index:
            folders = os.path.join(
                *argv[d_flag_index + 1:f_flag_index]
            )
        else:
            folders = os.path.join(
                *argv[d_flag_index + 1:]
            )
    if d_appeared:
        os.makedirs(folders, exist_ok=True)
    if f_appeared:
        if d_appeared:
            file_path = os.path.join(folders, file_path)
        file_existed = os.path.isfile(file_path)
        with open(file_path, "a") as file:
            if file_existed:
                file.write("\n")
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            row_number = 1
            row = input("Enter content line: ")
            while row != "stop":
                file.write(f"{row_number} {row}\n")
                row_number += 1
                row = input("Enter content line: ")


if __name__ == "__main__":
    create_file(argv)
