import sys
import os

from datetime import datetime


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_file(path: os) -> None:
    with open(path, "w") as f:
        f.write(f'{datetime.now().strftime("%m-%d-%Y %H:%M:%S")}\n')
        new_content = input("Enter new line of content: ")

        number_string = 1
        while new_content != "stop":
            f.write(f"{number_string} {new_content}\n")
            new_content = input("Enter new line of content: ")
            number_string += 1


def create_dictionary(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


path = sys.argv
if path[1] == "-d" and path[-2] == "-f":
    create_dictionary(create_path(path[2:-2]))
    del [path[-2]]
    create_file(create_path(path[2:]))

if path[1] == "-d":
    create_dictionary(create_path(path[2:]))

if path[1] == "-f":
    create_file(path[-1])
