import sys
import os
from datetime import datetime


def create_directory(args: list) -> str | bytes:
    path = os.path.join(*args)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_name: str, path: str = ".") -> None:
    file_path = os.path.join(path, file_name)
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        number_of_line = 1
        while True:
            content_line = input(f"Enter content line {number_of_line}: ")
            if content_line.lower() == "stop":
                break
            file.write(f"{number_of_line} {content_line}\n")
            number_of_line += 1


def main() -> None:
    command = sys.argv
    if "-f" in command and "-f" in command:
        path = create_directory(command[2:-2])
        create_file(command[-1], path)
    elif "-d" in command:
        create_directory(command[2:])
    elif "-f" in command:
        create_file(command[-1])
