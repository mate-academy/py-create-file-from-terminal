import os
import sys
from datetime import datetime
from typing import TextIO


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_directory(path: str) -> None:
    os.makedirs(path)


def write_in_file_text(source_file: TextIO) -> None:
    input_text = input("Enter content line: ")
    count = 0
    source_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    while input_text != "stop":
        count += 1
        source_file.write(f"{count} {input_text}\n")
        input_text = input("Enter content line: ")
    source_file.write("\n")


def create_file_or_directory(command_list: list) -> None:
    directories = []
    path = ""
    if "-d" in command_list:
        for command in command_list[2:]:
            if command == "-f":
                break
            directories.append(command)
        path = create_path(directories)
        if not os.path.exists(path):
            create_directory(path)

    if "-f" in command_list:
        path_file = (
            f"{path}/{command_list[-1]}"
            if directories
            else command_list[-1]
        )
        if os.path.exists(path_file):
            with open(path_file, "a") as source_file:
                write_in_file_text(source_file)
        else:
            with open(path_file, "w") as source_file:
                write_in_file_text(source_file)


commands = sys.argv

create_file_or_directory(commands)
