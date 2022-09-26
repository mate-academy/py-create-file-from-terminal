import os
import sys
from datetime import datetime


def parse_commands() -> None:
    commands = sys.argv

    if "-d" in commands and "-f" in commands:
        index_d = commands.index("-d")
        index_f = commands.index("-f")
        file_path = commands[index_d + 1: index_f]
        file_name = commands[index_f + 1:]
        create_directory(file_path)
        create_file(file_path + file_name)
    elif "-f" in commands:
        index_f = commands.index("-f")
        file_name = commands[index_f + 1:]
        create_file(file_name)
    elif "-d" in commands:
        index_d = commands.index("-d")
        file_path = commands[index_d + 1:]
        create_directory(file_path)


def create_directory(path_list: list) -> None:
    path = "/".join(path_list)
    os.makedirs(path)


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


parse_commands()
