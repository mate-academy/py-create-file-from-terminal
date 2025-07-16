import sys
import os
from datetime import datetime


def create_dir(parts: list, num_of_dirs: int) -> str:
    my_path = os.getcwd()
    my_path = os.path.join(my_path, *parts[2:num_of_dirs])
    os.makedirs(my_path)
    return my_path


def create_file_with_content(parts: list, my_path: str) -> None:
    content = []
    while True:
        command = input("Enter content line: ")
        if command == "stop":
            break
        content.append(command)
    file_name = parts[parts.index("-f") + 1]
    my_path = os.path.join(my_path, file_name)
    with open(my_path, "w") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for line in content:
            file.write(f"{line}\n")


def create_file() -> None:
    parts = sys.argv
    if parts[1] == "-d" and "-f" not in parts:
        create_dir(parts, len(parts))
    elif parts[1] == "-f" and "-d" not in parts:
        my_path = os.getcwd()
        create_file_with_content(parts, my_path)
    elif "-d" in parts and "-f" in parts:
        create_file_with_content(parts, create_dir(parts, parts.index("-f")))
