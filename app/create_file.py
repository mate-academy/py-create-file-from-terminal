import os
import sys
from datetime import datetime


DEFAULT_NAME = "file.txt"


def create_and_enter_data_into_file() -> None:
    command = sys.argv[1:]
    name = find_name(command)
    path = find_path_in_command(command)
    enter_data_into_file(str(path), name)


def find_name(command: list) -> str:
    index_before_name = find_f(command)
    if index_before_name:
        return command[index_before_name + 1]
    return DEFAULT_NAME


def find_path_in_command(commands: list) -> str:
    path = os.getcwd()

    if find_d(commands):
        del commands[find_d(commands)]

    if find_f(commands):
        del commands[commands.index(find_name(commands))]
        del commands[find_f(commands)]

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
    path_file = os.path.join(path, name)
    with open(path_file, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                break
            file.write(f"{content}\n")


create_and_enter_data_into_file()
