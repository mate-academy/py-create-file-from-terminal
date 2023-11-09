import os

import sys

from datetime import datetime


def create_directory(directories: list) -> None:

    if directories:
        base_directory = os.path.normpath(directories[0])

        os.makedirs(base_directory)

        for directory in directories[1:]:
            base_directory = os.path.join(base_directory, directory)
            os.makedirs(base_directory)
        os.chdir(base_directory)


def create_file(file_name: str, path: str) -> None:

    content_file = []

    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        content_file.append(f"\n{user_input}")

    with open(os.path.join(path, file_name), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        file.write(" ".join(content_file))
        file.write("\n\n")


if __name__ == "__main__":

    command = sys.argv

    if "-d" in command and "-f" not in command:

        d_index = command.index("-d")
        directories = command[d_index + 1:]
        create_directory(directories)

    elif "-f" in command and "-d" not in command:

        f_index = command.index("-f")
        file_name = command[f_index + 1]
        path = os.getcwd()
        create_file(file_name, path)

    elif "-f" in command and "-d" in command:

        d_index = command.index("-d")
        f_index = command.index("-f")
        directories = command[d_index + 1:f_index]
        file_name = command[f_index + 1]
        create_directory(directories)
        path = os.getcwd()
        create_file(file_name, path)
