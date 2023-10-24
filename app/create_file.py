import os
import sys
from datetime import datetime


NAME_OF_FILE_BY_DEFAULT = "file.txt"


def main_func_create_and_enter_data_into_file() -> None:
    command = sys.argv[1:]
    name = find_name_in_command(command)
    path = find_path_in_command(command)
    enter_data_into_file(str(path), name)


def find_name_in_command(command: list) -> str:
    index_before_name = find_f(command)
    if index_before_name:
        return command[index_before_name + 1]
    return NAME_OF_FILE_BY_DEFAULT


def find_path_in_command(commands: list) -> str:
    path = os.getcwd()

    if find_d(commands):
        commands.pop(find_d(commands))

    if find_f(commands):
        commands.pop(commands.index(find_name_in_command(commands)))
        commands.pop(find_f(commands))

    for command in commands:
        path = os.path.join(path, command)
        if os.path.exists(path):
            continue
        os.mkdir(path)
    return str(path)


def find_f(command: list) -> int:
    if "-f" in command:
        return command.index("-f")


def find_d(command: list) -> int:
    if "-d" in command:
        return command.index("-d")


def enter_data_into_file(path: str, name: str) -> None:
    path_to_file = os.path.join(path, name)
    with open(path_to_file, "a") as source_file:
        source_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                source_file.write("\n")
                break
            source_file.write(f"{content_line}\n")


main_func_create_and_enter_data_into_file()
