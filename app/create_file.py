import datetime
import os
import sys


def file_from_terminal() -> None:
    input_command = sys.argv

    if "-d" in input_command and "-f" in input_command:
        create_directory(input_command[2:-2])
        create_file(input_command[-1])
        return

    if "-d" in input_command:
        create_directory(input_command[2:])

    if "-f" in input_command:
        create_file(input_command[2])


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file_time = datetime.datetime.now().strftime(
            "%y-%m-%d %H:%M:%S\n")
        file.write(file_time)

        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(text + "\n")


def create_directory(directories: list) -> None:
    for directory in directories:
        os.mkdir(directory)
        os.chdir(directory)


file_from_terminal()
