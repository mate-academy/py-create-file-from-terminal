import sys
import os
from datetime import datetime
from typing import Tuple, Any, List


def create_directory(directory: list) -> None:
    dir_path = os.path.join(*directory)
    os.makedirs(dir_path, exist_ok=True)


def parse(commands: list) -> tuple[str | Any, list[Any]]:
    file_name = ""
    dir_path = []

    if "-f" in commands:
        file_name = commands.pop(commands.index("-f") + 1)

    for command in commands:
        if command in ["-f", "-d"]:
            continue

        dir_path.append(command)

    return file_name, dir_path


def create_file() -> None:
    commands = sys.argv[1:]
    filename, dir_path = parse(commands)

    content = ""
    counter_of_lines = 1

    if dir_path:
        create_directory(dir_path)

    if filename:
        filename = os.path.join(*dir_path, filename)
        file_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        content = f"{file_time}\n"
        counter_of_lines = 1

    while True:
        user_input = input(f"Enter content: ")

        if user_input == "stop":
            content += "\n"
            break
        content += f"{counter_of_lines} {user_input}\n"
        counter_of_lines += 1

    with open(filename, "a") as file:
        file.write(content)


if __name__ == "__main__":
    create_file()