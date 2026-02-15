import os
import sys
import datetime
from typing import Union


def create_dir(*parts) -> str:
    if no *parts:
        raise TypeError("No path was given")
    for part in parts:
        if not isinstance(part, str):
            raise ValueError("path parts must be str")
    dir_path = os.path.join(*parts)
    os.makedirs(dir_path, exist_ok=True)
    return str(dir_path)


def write_to_file(file_name: str, writing_type: str) -> None:
    line_count = 0
    with open(file_name, writing_type) as file:
        if writing_type == "a":
            file.write("\n")
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                   + "\n")
        while True:
            line_count += 1
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                break
            file.write(f"{line_count} {user_input}\n")


def create_file_no_dir(file_path: str) -> None:
    if os.path.exists(file_path):
        mode = "a"
    else:
        mode = "w"
    write_to_file(file_path, mode)


def create_file_dir(arguments: list) -> Union[None, str]:
    try:
        if "-f" in arguments:
            end_index = arguments.index("-f")
            dirs = arguments[2:end_index]
        else:
            dirs = arguments[2:]
        dir_path = create_dir(*dirs)
        return dir_path
    except IndexError:
        print("Not enough arguments")
        return None


def create_file_and_dir(arguments: list) -> None:
    dir_path = create_file_dir(arguments)
    if dir_path is None:
        return None
    file_name = arguments[-1]
    file_path = os.path.join(dir_path, file_name)
    create_file_no_dir(file_path)


def creation(file_creation_input: list) -> None:
    if len(file_creation_input) < 2:
        raise IndexError("Not enough arguments")
    if file_creation_input[1] == "-d" and "-f" in file_creation_input:
        create_file_and_dir(file_creation_input)
    elif file_creation_input[1] == "-f":
        file_name = file_creation_input[2]
        create_file_no_dir(file_name)
    elif file_creation_input[1] == "-d":
        create_file_dir(file_creation_input)


creation(sys.argv)
