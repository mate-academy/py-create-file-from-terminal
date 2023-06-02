import sys
import os
from datetime import datetime as dt


path_list = sys.argv
now = dt.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
new_file = path_list[path_list.index("-f") + 1]
folders = path_list[2: path_list.index("-f")]


def create_folders() -> None:
    os.makedirs(os.path.join(*folders), exist_ok=True)


def create_file_with_content() -> None:
    with open(new_file, "a") as f:
        f.write(f"{timestamp}\n")
        while True:
            line = input("Enter content line:")
            if line == "stop":
                break
            f.write(f"{line}\n")


if "-d" in path_list and "-f" not in path_list:
    folders = path_list[2:]
    create_folders()
elif "-d" not in path_list and "-f" in path_list:
    new_file = path_list[path_list.index("-f") + 1:]
    create_file_with_content()
elif "-d" in path_list and "-f" in path_list:
    new_file = os.path.join(*folders, new_file)
    create_folders()
    create_file_with_content()
