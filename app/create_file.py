import os
import sys
from datetime import datetime


command = sys.argv


def make_dir() -> None:
    os.makedirs("/".join(command[2:]))


def create_file(directory: str = "") -> None:
    with open(f"{directory}{command[-1]}", "w") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line = 1
        while True:
            line_text = input("Enter content line: ")

            if line_text == "stop":
                file.write("\n")
                break
            file.write(f"{line} {line_text}\n")
            line += 1


def create_file_in_directory() -> None:
    direc_file = "/".join(command[2: command.index("-f")])
    os.makedirs(direc_file)
    create_file(f"{direc_file}/")


if "-d" in command and "-f" not in command:
    make_dir()

elif "-f" in command and "-d" not in command:
    create_file()

elif "-f" in command and "-d" in command:
    create_file_in_directory()
