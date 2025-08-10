import os
import sys
from datetime import datetime


def get_path_file(arg: list[str]) -> tuple:
    type_elem = ""
    is_path = []
    is_file = ""
    for elem in sys.argv:
        if elem == "-d":
            type_elem = "path"
            continue
        if elem == "-f":
            type_elem = "file"
            continue
        if type_elem == "path":
            is_path.append(elem)
        if type_elem == "file":
            is_file = elem
    return is_path, is_file


def make_path(is_path: list[str]) -> str:
    if is_path:
        path = os.path.join(*is_path)
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    return ""


def write_content(file_: object) -> None:
    num_line = 0
    while True:
        content = input("Enter content line: ")
        num_line += 1
        if content == "stop":
            file_.write("\n")
            break
        file_.write(f"{num_line} {content} \n")


def make_file(path: str, is_file: str) -> None:
    if is_file:
        with open(os.path.join(path, is_file), "a") as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{current_time} \n")
            write_content(file)


is_path, is_file = get_path_file(sys.argv)
path = make_path(is_path)
make_file(path, is_file)
