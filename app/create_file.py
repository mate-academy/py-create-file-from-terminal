import os
import sys
from datetime import datetime


def create_dir(dir_name: list) -> str:
    dir_name2 = ""
    for dir_ in dir_name:
        dir_name2 = os.path.join(dir_name2, dir_)
        if not os.path.exists(dir_name2):
            os.makedirs(dir_name2)
    print(dir_name2)
    return str(dir_name2)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S" + "\n"))
        while True:
            str_input = input("Enter content line: ")
            if str_input == "stop":
                f.write("\n")
                break
            f.write(str_input + "\n")


def get_and_executing_command() -> None:
    full_command = sys.argv
    start_dir, end_dir, start_file = 0, 0, 0
    for i, part_command in enumerate(full_command):
        if "-d" == part_command:
            start_dir = i + 1
            end_dir = len(full_command)
        if "-f" == part_command:
            end_dir = i
            start_file = i + 1
    if start_dir != 0 and end_dir != 0 and start_file != 0:
        where = create_dir(full_command[start_dir:end_dir])
        create_file(os.path.join(str(where), full_command[start_file]))
        return
    if start_dir != 0 and end_dir != 0:
        create_dir(full_command[start_dir:end_dir])
        return
    if start_file != 0:
        create_file(os.path.join(os.getcwd(), full_command[start_file]))


get_and_executing_command()
