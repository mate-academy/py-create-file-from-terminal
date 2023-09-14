import datetime
import os
import sys
from typing import Any


def write_content_to_file(file_name: Any) -> None:

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        file_name.write(line + "\n")


commands = sys.argv


def create_path(directory_path: list) -> None:
    if "-d" in commands:
        directory_path = commands[commands.index("-d") + 1:]
        path = os.path.join(*directory_path)

        if not os.path.exists(path):
            os.makedirs(path)


def create_file(file_name: str) -> None:
    file_data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if "-f" in commands:
        file_name = str(commands[commands.index("-f") + 1:])

        with open(file_name, "w") as file:
            file.write(f"{file_data}\n")
            write_content_to_file(file)

        if os.path.exists(file_name):
            with open(file_name, "a") as exists_file:
                exists_file.write(f"\n{file_data}\n")
                write_content_to_file(exists_file)


def create_file_and_path() -> None:
    if "-d" in commands and "-f" in commands:
        directory_path = commands[commands.index("-d") + 1:]
        file_name = str(commands[commands.index("-f") + 1:])
        create_path(directory_path)
        create_file(file_name)
