import os
import sys
from datetime import datetime


def create_dirs(paths: list) -> str:
    path = os.path.join(*paths)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(*args) -> None:
    line_number = 1
    with open(os.path.join(*args), "a+") as result_file:
        result_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                result_file.write("\n")
                break
            result_file.write(f"{line_number} {content_line}\n")
            line_number += 1


def full_creation() -> None:
    input_lst = sys.argv
    if "-f" not in input_lst:
        paths = input_lst[(input_lst.index("-d") + 1):]
        create_dirs(paths)
    if "-d" in input_lst and "-f" in input_lst:
        file_name = input_lst[input_lst.index("-f") + 1]
        paths = input_lst[(input_lst.index("-d") + 1):input_lst.index("-f")]
        create_file(create_dirs(paths), file_name)
    if "-d" not in input_lst:
        file_name = input_lst[input_lst.index("-f") + 1]
        create_file(file_name)
