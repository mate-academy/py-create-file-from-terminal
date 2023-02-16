import os
import sys
from datetime import datetime


commands = sys.argv[1:]


def create_directories(path: list) -> None:
    if "-d" in path and "-f" in path:
        directories = path[1:path.index("-f")]
    else:
        directories = path[1:]
    directories_path = os.path.join(*directories)
    os.makedirs(directories_path, exist_ok=True)
    os.chdir(directories_path)


def create_file(path: list) -> None:
    file_name = path[-1]
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
if "-d" in commands:
    create_directories(commands)

# File creation:
if "-f" in commands:
    create_file(commands)
