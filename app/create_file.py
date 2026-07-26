import sys
import os
from datetime import datetime as dt


def create_path(folders: list) -> bytes | str:
    path = os.path.join(*folders)
    return path


def create_file(system_argument: list, index: int) -> None:
    with open(system_argument[index + 1], "a+") as file:
        file.write(f"{dt.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        number_line = 0
        while True:
            line = input("Enter content line: ")
            number_line += 1
            if line == "stop":
                break
            file.write(f"{number_line} {line}\n")


def create_folder(system_argument: list, index: int) -> None:
    folders = []
    for folder in range(len(system_argument[index:]) - 1):
        if system_argument[index:][folder + 1] == "-f":
            try:
                os.makedirs(create_path(folders))
                os.chdir(create_path(folders))
            except FileExistsError:
                os.chdir(create_path(folders))
        folders.append(system_argument[index:][folder + 1])


def start_create(system_argument: list) -> None:
    for index in range(len(system_argument)):
        if system_argument[index] == "-f":
            create_file(system_argument, index)
        if system_argument[index] == "-b":
            create_folder(system_argument, index)


if __name__ == "__main__":
    start_create(sys.argv)
