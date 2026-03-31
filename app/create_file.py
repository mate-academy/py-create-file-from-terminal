from datetime import datetime

import sys
import os


def create_path(list_of_agrs: list) -> str:
    path = ""
    flag_d = list_of_agrs.index("-d")
    flag_f = len(list_of_agrs)
    if "-f" in list_of_agrs:
        flag_f = list_of_agrs.index("-f")
    dir_list = list_of_agrs[flag_d + 1: flag_f]
    for part in dir_list:
        path = os.path.join(path, part)
    try:
        os.makedirs(path)
    except OSError:
        pass
    return path


def create_file(file_name: str, file_path: str) -> None:
    tag = "w"
    if file_name in os.listdir(file_path):
        tag = "a"
    file_with_path = os.path.join(file_path, file_name)
    with open(file_with_path, tag) as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        input_text = input("Enter content line: ")
        line_number = 1
        while input_text != "stop":
            file.write(f"{line_number} {input_text}\n")
            input_text = input("Enter content line: ")
            line_number += 1
        file.write("\n")


command_list = sys.argv
path_to_file = ""
if "-d" in command_list:
    path_to_file = create_path(command_list)

if "-f" in command_list:
    file_name = command_list[command_list.index("-f") + 1]
    create_file(file_name, path_to_file)
