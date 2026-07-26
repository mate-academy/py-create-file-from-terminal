import sys
import os
from datetime import datetime


def flag_check():
    args = sys.argv
    if "-d" in args and "-f" in args:
        path_list = args[2:-2]
        file_name = args[-1]
        new_path = create_path(path_list)
        new_dir = os.path.join(new_path, file_name)
        create_file(new_dir)
    if "-d" in args:
        create_path(args[2:])
    if "-f" in args:
        create_file(args[2])


def create_path(dir_list: list):
    new_path = os.path.join(*dir_list)
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    return new_path


def create_file(filename: str):
    with open(filename, "a") as new_file:
        number = 1

        current_time = datetime.datetime.now()
        current_date = current_time.strftime("%Y-%m-%d %H:%M:%S")

        new_file.write(current_date + "\n")

        while True:
            line = input("Enter content line: ")

            if line == "stop":
                new_file.write("\n")
                break
            else:
                new_file.write(f"{number} {line}\n")
                number += 1
