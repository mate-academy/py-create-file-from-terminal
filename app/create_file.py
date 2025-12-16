from datetime import datetime
from typing import LiteralString
import os
import sys


def create_app(command: list) -> None:
    directories, file_name = get_files_and_directories(command)
    destination_path = os.path.join(directories, file_name)

    if "-d" in command:
        create_directories(directories)

    if "-f" in command:
        create_file(destination_path)


def get_files_and_directories(command: list) -> tuple:
    dirs = ""
    file_name = None

    current = None
    for token in command:
        if token == "-d":
            current = "-d"
        elif token == "-f":
            current = "-f"
        else:
            if current == "-d":
                dirs += f"{token}/"
            if current == "-f":
                file_name = token
    return dirs, file_name


def create_directories(directories: str) -> None:
    destination_path = os.path.join(directories)
    try:
        os.mkdir(destination_path)
        os.makedirs(destination_path, exist_ok=True)
    except OSError:
        pass


def create_file(destination_path: LiteralString | str | bytes) -> None:
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(destination_path, "a") as file:
            file.write(f"{time_now}\n")
            while True:
                user_input = input("Enter content line: ")
                if user_input == "stop":
                    break
                file.write(f"{user_input}\n")
    except OSError:
        raise


if __name__ == "__main__":
    create_app(sys.argv)
