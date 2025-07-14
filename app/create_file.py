import os
import sys
from datetime import datetime


def create_directory(lst):
    parent_dir = os.getcwd()
    d_index = lst.index("-d")
    if "-f" in lst:
        f_index = lst.index("-f")
        dir_path = lst[d_index + 1:f_index]
    else:
        dir_path = lst[d_index + 1:]
    path = os.path.join(parent_dir, *dir_path)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(lst, path):
    if "-d" in lst:
        file_path = f"{path}/{lst[lst.index('-f') + 1]}"
    else:
        f_index = lst.index("-f")
        file_path = lst[f_index + 1]
    with open(file_path, "a") as file:
        current_date = datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S\n"))
        count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{count} {line}\n")
            count += 1
        file.write("\n")


lst = sys.argv

if "-d" in lst and "-f" in lst:
    path = create_directory(lst)
    create_file(lst, path)

if lst[1] == "-d":
    create_directory(lst)

if lst[1] == "-f":
    create_file(lst, None)
