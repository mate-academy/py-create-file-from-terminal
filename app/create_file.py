import os
import sys
from datetime import datetime


def create_directory(dir_path: str) -> None:
    os.makedirs(dir_path)


def create_file(file_path_and_name: str) -> None:
    with open(f"{file_path_and_name}", "a") as new_file:
        (
            new_file.write(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            )
            if os.path.getsize(file_path_and_name) == 0
            else new_file.write(
                "\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            )
        )

        line = 0
        while True:
            line += 1
            content = input("Enter content line: ")
            if content == "stop":
                break
            new_file.write(f"{line} " + content + "\n")


def create_directory_and_file(
        directory: str,
        file_name: str
) -> None:
    os.makedirs(directory)
    dir_and_file_path = os.path.join(directory, file_name)
    create_file(dir_and_file_path)


commands = sys.argv

if "-d" in commands and "-f" in commands:
    index_d = commands.index("-d")
    index_f = commands.index("-f")
    directories = os.path.join(*commands[(index_d + 1):index_f])
    file = commands[index_f + 1]

    create_directory_and_file(directories, file)

elif "-d" in commands:
    index = commands.index("-d")
    directories = os.path.join(*commands[(index + 1):])

    create_directory(directories)

elif "-f" in commands:
    index = commands.index("-f")
    file_path_and_name = commands[index + 1]

    create_file(file_path_and_name)
