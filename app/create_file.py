import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    time = datetime.now()
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_input(path: str) -> None:
    line_number = 0
    with open(path, "a") as file:
        file.write("\n" + get_timestamp() + "\n")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                # file.write("\n")
                break
            line_number += 1
            file.write(f"{line_number} {line}\n")


def create_path() -> str | None:
    current_dir = ""
    command = sys.argv[1:]
    if "-d" in command:
        directories = command[
            1: command.index("-f") if "-f" in command else len(command)
        ]
        current_dir = directories[0]
        for directory in directories[1:]:
            current_dir = os.path.join(current_dir, directory)
        if not os.path.exists(current_dir):
            os.makedirs(current_dir)
    if "-f" in command:
        filename = os.path.join(current_dir, command[-1])
        return filename


def create_file_from_terminal() -> None:
    filename = create_path()
    if filename:
        get_input(filename)


if __name__ == "__main__":
    create_file_from_terminal()
