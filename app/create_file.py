import sys
import os
from datetime import datetime


def create_directory(path: list) -> None:
    path_ = os.path.join(*path)
    os.makedirs(path_, exist_ok=True)
    os.chdir(path_)


def create_file(file_name: str) -> None:
    content = []
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content.append(content_line)

    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for idx, line in enumerate(content, start=1):
            file.write(f"{idx} {line}\n")


def create_file_from_terminal() -> None:
    command = sys.argv[1:]
    directory_name = command[1:]
    file_name = command[-1]

    if "-f" in command:
        if "-d" in command:
            directory_name = command[1:command.index("-f")]
            create_directory(directory_name)
        create_file(file_name)
    else:
        create_directory(directory_name)


create_file_from_terminal()
