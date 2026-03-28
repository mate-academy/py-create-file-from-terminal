import os
import sys
import datetime


command = sys.argv[1:]


def get_f_index(command: str) -> int:
    if "-f" in command:
        return command.index("-f")


def get_d_index(command: str) -> int:
    if "-d" in command:
        return command.index("-d")


def get_file_name(command: list) -> str:
    f_index = get_f_index(command)
    if f_index is not None:
        return command[f_index + 1]
    return "file.txt"


def get_path_parts(command: list) -> list:
    if get_d_index(command) is not None:
        command.pop(get_d_index(command))
    if get_f_index(command) is not None:
        command.pop(command.index(get_file_name(command)))
        command.pop(get_f_index(command))
    return command


def create_path(path_parts: list) -> str:
    path = os.getcwd()
    for part in path_parts:
        path = os.path.join(path, part)
        if os.path.exists(path):
            continue
        os.mkdir(path)
    return path


def write_in_file(path: str, file_name: str) -> None:
    file_path = os.path.join(path, file_name)
    with open(file_path, "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"\n{line}")


def create_and_write_file(command: str) -> None:
    file_name = get_file_name(command)
    path_parts = get_path_parts(command)
    path = create_path(path_parts)
    write_in_file(path, file_name)


create_and_write_file(command)
