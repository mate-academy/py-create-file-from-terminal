import sys
import os
from datetime import datetime


def create_file_or_dir() -> None:

    terminal_command = sys.argv
    makedir_index = makefile_index = 0
    dir_list = file_name = None

    try:
        if "-f" in terminal_command:
            makefile_index = terminal_command.index("-f")
            file_name = terminal_command[makefile_index + 1]

        if "-d" in terminal_command:
            makedir_index = terminal_command.index("-d")
            dir_list = terminal_command[makedir_index + 1:]

        if makefile_index and makedir_index:
            if makefile_index - makedir_index > 1:
                dir_list = terminal_command[makedir_index + 1: makefile_index]
            elif abs(makefile_index - makedir_index) == 1:
                raise ValueError
            create_directory(create_path(dir_list))
            create_file(create_path(dir_list), file_name)

        if makedir_index and not makefile_index:
            create_directory(create_path(dir_list))

        if makefile_index and not makedir_index:
            create_file("", file_name)

    except ValueError:
        print("Bad format command or no-valid value.")
        print("Use: python create.py -d <directory`s name> -f <filename.txt>")
        print("or: python create.py -f <filename.txt> -d <directory`s name>")


def create_path(dirs: list) -> str:
    path = os.path.join(*dirs)
    return path


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(path: str, filename: str) -> None:
    f_name = os.path.join(path, filename)
    with open(f_name, "a") as f:
        f.write(f'{datetime.now().strftime("%m-%d-%Y %H:%M:%S")}\n')
        line_content = input("Enter new line of content: ")

        num_line = 1
        while line_content != "stop":
            f.write(f"{num_line} {line_content}\n")
            line_content = input("Enter new line of content: ")
            num_line += 1


create_file_or_dir()
