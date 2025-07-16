import sys
import os
from datetime import datetime


def create_dir(parts: list, num_of_dirs: int) -> None:
    my_path = os.getcwd()
    os.path.join(my_path, *parts[2:num_of_dirs])
    os.makedirs(my_path)


def create_file_with_content(parts: list) -> None:
    content = []
    while True:
        command = input("Enter content line: ")
        if command == "stop":
            break
        content.append(command)
    file_name = parts[parts.index("-f") + 1]
    with open(file_name, "r") as file:
        file.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
        for line in content:
            file.write(f"{line}\n")


def create_file() -> None:
    parts = sys.argv
    if parts[1] == "-d" and "-f" not in parts:
        create_dir(parts, len(parts))
    elif parts[1] == "-f" and "-d" not in parts:
        create_file_with_content(parts)
    elif "-d" in parts and "-f" in parts:
        create_dir(parts, parts.index("-f"))
        create_file_with_content(parts)
