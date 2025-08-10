import sys
import os
from datetime import datetime


def create_directory(directory_path: list) -> None:
    path = os.path.join(*directory_path)
    os.makedirs(path, exist_ok=True)


def input_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{date_now}\n")
        line_number = 1
        while True:
            input_message = input("Enter content line: ")
            if input_message == "stop":
                break
            f.write(f"{line_number} {input_message}\n")
            line_number += 1


def create_directory_or_file() -> None:
    args_list = sys.argv[1:]

    if "-d" in args_list and "-f" in args_list:
        d_index = args_list.index("-d")
        f_index = args_list.index("-f")
        directory_path = args_list[d_index + 1: f_index]
        file_name = args_list[f_index + 1]

        if directory_path:
            create_directory(directory_path)
            input_file(file_name)

    if "-d" in args_list:
        d_index = args_list.index("-d")
        directory_path = args_list[d_index + 1:]

        if directory_path:
            create_directory(directory_path)

    if "-f" in args_list:
        f_index = args_list.index("-f")
        file_name = args_list[f_index + 1]

        input_file(file_name)
