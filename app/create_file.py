import os
import sys

from datetime import datetime


def create_path(path: list) -> None:
    path = os.path.join(" ".join(path))
    os.makedirs(path, exist_ok=True)
    os.chdir(path)


def create_file(name: str) -> None:
    with open(name, "a") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line = input("Enter content line: ")
        row = 1
        while line.lower() != "stop":
            new_file.write(f"{row} {line}\n")
            row += 1
            line = input("Enter content line: ")


def create_file_from_terminal() -> None:
    command = sys.argv[1::]
    d_start_index = command.index("-d")
    f_start_index = command.index("-f")
    file_name = command[-1]
    path = command[d_start_index + 1: f_start_index]

    if "-d" in command and "-f" in command:
        create_path(path)
        create_file(file_name)

    if "-f" in command and "-d" not in command:
        create_file(file_name)

    if "-d" in command and "-f" not in command:
        create_path(path)


create_file_from_terminal()
