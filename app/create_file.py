import datetime
import os
import sys


def file_from_terminal() -> None:
    user_input = sys.argv

    if "-d" in user_input and "-f" in user_input:
        work_with_directory(user_input[2:-2])
        work_with_file(user_input[-1])
        return

    if "-d" in user_input:
        work_with_directory(user_input[2:])

    if "-f" in user_input:
        work_with_file(user_input[2])


def work_with_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file_time = datetime.datetime.now().strftime(
            "%y-%m-%d %H:%M:%S\n")
        file.write(file_time)

        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(text + "\n")


def work_with_directory(directories: list) -> None:
    for directory in directories:
        os.mkdir(directory)
        os.chdir(directory)


file_from_terminal()
