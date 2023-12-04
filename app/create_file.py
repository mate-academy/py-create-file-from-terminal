import sys

import os

from datetime import datetime
from time import strftime


def write_to_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        if os.stat(file_name).st_size != 0:
            file.write(strftime("\n" + str(datetime.now())) + "\n")
        else:
            file.write(strftime(str(datetime.now())) + "\n")

        while True:
            data_input = input("Enter content line: ")
            if data_input == "stop":
                break
            file.write(data_input + "\n")


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_text_file() -> None:
    command = list(sys.argv)
    path_to_file = []

    if "-d" in command:
        for element in command:
            if element == "-f":
                break
            path_to_file.append(element)

        path_to_file = path_to_file[2:]
        file_path = create_path(path_to_file)
        os.makedirs(file_path) if not os.path.exists(file_path) else None

    path_to_file.append(command[-1])

    write_to_file(create_path(path_to_file))


if __name__ == "__main__":
    create_text_file()
