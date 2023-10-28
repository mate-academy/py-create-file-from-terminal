import sys
import os
from datetime import datetime


def write_content_to_file(path_and_file_name: list[str]) -> None:
    with open(os.path.join(*path_and_file_name), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_input = 0
        count_of_iteration = 1
        line_input = input("Enter content line:")
        while line_input != "stop":
            file.write(str(count_of_iteration) + " " + line_input + "\n")
            count_of_iteration += 1
            line_input = input("Enter content line:")
        file.write("\n")


def create_dirs(dirs_names: list[str]) -> str:
    if not dirs_names:
        return ""
    path = os.path.join(*dirs_names)
    if not os.path.isdir(path):
        os.makedirs(path)
    return path


def read_terminal_content() -> None:
    params = sys.argv
    dirs = []
    flag = 0
    file_name = ""
    for param in params:
        if param == "-f":
            flag = "-f"
        if param == "-d":
            flag = "-d"
        if flag == "-d" and param != "-d":
            dirs.append(param)
        if flag == "-f" and param != "-f":
            file_name = param

    path = create_dirs(dirs)
    if flag == "-f":
        write_content_to_file([path, file_name])


read_terminal_content()
