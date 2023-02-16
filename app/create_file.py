import os
import sys
from datetime import datetime


cmd = sys.argv[1:]


def create_directories(path: list) -> str:
    directories = []
    for directory in path[path.index("-d") + 1:]:
        if directory == "-f":
            break
        directories.append(directory)
    directories_path = os.path.join(*directories)
    os.makedirs(directories_path, exist_ok=True)
    if "-f" in cmd:
        return directories_path


def create_file(path: list) -> None:
    if "-d" in cmd:
        file_name = f"{create_directories(path)}\\{path[path.index('-f') + 1]}"
    else:
        file_name = path[path.index("-f") + 1]
    open_type = "w" if not os.path.exists(file_name) else "a"
    with open(file_name, open_type) as file_in:
        file_in.write(
            f"{datetime.now().strftime('%Y-%m-%d %I:%M:%S')}\n"
        )
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file_in.write(f"{line_number} {content}\n")
            line_number += 1
        file_in.write("\n")


# Directories creation:
if "-d" in cmd:
    create_directories(cmd)

# File creation:
if "-f" in cmd:
    create_file(cmd)
