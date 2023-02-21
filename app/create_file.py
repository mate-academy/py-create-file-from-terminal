import os
import sys
from datetime import datetime


command = sys.argv


def make_dir() -> None:
    os.makedirs("/".join(command[2:]))


def create_file() -> None:
    with open(command[-1], "w") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            line_text = input("Enter content line: ")
            if line_text == "stop":
                break
            file.write(f"1 {line_text}\n")


def create_file_in_directory() -> None:
    os.makedirs("/".join(command[2: command.index("-f")]))

    with open(f"{'/'.join(command[2: command.index('-f')])}/{command[-1]}",
              "w") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            line_text = input("Enter content line: ")
            if line_text == "stop":
                break
            file.write(f"1 {line_text}\n")


if "-d" in command and "-f" not in command:
    make_dir()

elif "-f" in command and "-d" not in command:
    create_file()

elif "-f" in command and "-d" in command:
    create_file_in_directory()
