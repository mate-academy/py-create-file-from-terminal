import os
import sys
from datetime import datetime
from pathlib import Path


class PathError(Exception):
    pass


def create_directory(path: list) -> Path:
    directory = os.path.join(*path)
    os.makedirs(directory, exist_ok=True)
    return Path(directory)


def fill_content() -> list:
    counter = 0
    content = []
    while True:
        counter += 1
        new_line = input("Enter content line: ")
        if new_line == "stop":
            content.append("\n")
            break
        content.append(f"{counter} {new_line}\n")
    return content


def write_to_the_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.writelines(fill_content())


def parse_arguments(arguments: list) -> Path:
    if "-d" in arguments and "-f" in arguments:
        for key, value in enumerate(arguments):
            if value == "-d":
                start = key
            elif value == "-f":
                end = key
        path_dir = create_directory(arguments[start + 1:end])
        file_name = path_dir / arguments[len(arguments) - 1]
        return file_name
    elif arguments[0] == "-f":
        file_name = arguments[1]
        return file_name
    elif arguments[0] == "-d":
        path_dir = create_directory(arguments[1:])
        file_name = path_dir / "file.txt"
        return file_name


def create_file() -> Path:
    try:
        arguments = sys.argv[1:]
        file_name = parse_arguments(arguments)
        write_to_the_file(file_name)
    except TypeError:
        raise PathError("Command is incorrect")
