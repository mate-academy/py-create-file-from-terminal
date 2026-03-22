import os
import sys
from datetime import datetime


def create_directory(directories: list) -> str:
    path = ""
    for directory in directories:
        path = os.path.join(path, directory)
    os.makedirs(path, exist_ok=True)

    return path


def create_file(filename: str) -> None:
    with open(filename, "a") as file:
        current_date = str(datetime.now().replace(microsecond=0))
        page_number = 1
        file.write(f"{current_date}\n")
        while True:
            text_input = input("Enter content line: ")

            if text_input == "stop":
                break

            file.write(f"{page_number} {text_input}\n")
            page_number += 1


command_elements = sys.argv
if "-d" in command_elements and "-f" in command_elements:
    d_index = command_elements.index("-d")
    f_index = command_elements.index("-f")

    if d_index < f_index:
        parts = command_elements[d_index + 1: f_index]
        path = create_directory(parts)
    else:
        parts = command_elements[d_index + 1:]
        path = create_directory(parts)

    filename = os.path.join(path, command_elements[f_index + 1])
    create_file(filename)

elif "-d" in command_elements:
    d_index = command_elements.index("-d")
    parts = command_elements[d_index + 1:]
    create_directory(parts)

elif "-f" in command_elements:
    f_index = command_elements.index("-f")
    filename = command_elements[f_index + 1]
    create_file(filename)
