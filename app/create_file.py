import os
import sys
from datetime import datetime


def create_directory_file() -> None:
    command = sys.argv

    if "-d" in command and "-f" in command:
        directory_flag = command.index("-d")
        file_flag = command.index("-f")

        directories = command[(directory_flag + 1): file_flag]
        file_name = command[-1]

        file_path = create_directory(directories) + file_name

        add_content(file_path)

    elif "-d" in command:
        directory_flag = command.index("-d")

        directories = command[(directory_flag + 1):]

        create_directory(directories)

    elif "-f" in command:
        file_name = command[-1]
        add_content(file_name)


def create_directory(directory_path: list[str]) -> str:
    directory_path = "/".join(directory_path)
    os.makedirs(directory_path)

    return directory_path + "/"


def add_content(path: str) -> None:
    current_time = datetime.strftime(datetime.now(), "%Y-%d-%m %H:%M:%S")

    with open(path, "w") as f:
        f.write(current_time + "\n")
        num_line = 0
        content = input("Enter content line:")
        while content.lower() != "stop":
            num_line += 1
            f.write(f"{num_line} Line{num_line} {content}\n")
            content = input("Enter content line:")


create_directory_file()
