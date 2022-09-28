import sys
import os

from datetime import datetime


def create_file(file_name: str, path: list = None) -> None:
    if path:
        os.makedirs("/".join(path))
        file_name = f"{'/'.join(path)}/{file_name}"

    with open(file_name, "a") as file:
        line_number = 1
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def create_file_from_terminal() -> None:
    command = sys.argv[1::]

    if "-d" in command and "-f" not in command:
        os.makedirs("/".join(command[1::]))

    if "-f" in command and "-d" not in command:
        file_to_create = command[-1]
        create_file(file_to_create)

    if "-f" in command and "-d" in command:
        directory_flag = command.index("-d")
        file_flag = command.index("-f")
        name = command[file_flag + 1]
        path = command[directory_flag + 1: file_flag]
        create_file(name, path)
