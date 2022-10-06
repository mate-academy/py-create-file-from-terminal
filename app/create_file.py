import sys
import os
from datetime import datetime


def create_from_terminal() -> None:
    command = sys.argv

    if "-d" in command and "-f" in command:
        index_d = command.index("-d")
        index_f = command.index("-f")
        file_path = command[index_d + 1: index_f]
        file_name = command[index_f + 1:]
        create_directory(file_path)
        create_file(file_path + file_name)
    elif "-f" in command:
        index_f = command.index("-f")
        file_name = command[index_f + 1:]
        create_file(file_name)
    elif "-d" in command:
        index_d = command.index("-d")
        file_path = command[index_d + 1:]
        create_directory(file_path)


def create_directory(path_list: list) -> None:
    path = "/".join(path_list)
    os.makedirs(path, exist_ok=True)


def create_file(path: list) -> None:
    path = "/".join(path) if isinstance(path, list) else path
    with open(path, "w") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time}\n")
        line_number = 1
        content_line = input("Enter content line: ")
        while content_line != "stop":
            f.write(f"{line_number} Line{line_number} {content_line}\n")
            line_number += 1
            content_line = input("Enter content line: ")


create_from_terminal()
