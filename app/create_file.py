import os
import sys
from datetime import datetime


def create_directory(commands: list) -> str:
    current_directory = ""
    for subdirectory in commands[2:]:
        if subdirectory == "-f":
            break
        current_directory = os.path.join(subdirectory, current_directory)
        os.mkdir(current_directory)
    return current_directory


def create_file(commands: list) -> None:
    new_file = os.path.join(create_directory(commands), sys.argv[-1])
    with open(new_file, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        create_directory(sys.argv)
        create_file(sys.argv)

    if "-d" in sys.argv:
        create_directory(sys.argv)

    if "-f" in sys.argv:
        create_file(sys.argv)
