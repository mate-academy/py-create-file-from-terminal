import os
import sys
from datetime import datetime


def create_dirs(dirs: list) -> str:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(*args) -> None:
    line_number = 1
    with open(os.path.join(*args), "a+") as result_file:
        result_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                result_file.write("\n")
                break
            result_file.write(f"{line_number} {content_line}\n")
            line_number += 1


def full_creation() -> None:
    terminal_command = sys.argv
    if "-d" not in terminal_command:
        file_name = terminal_command[terminal_command.index("-f") + 1]
        create_file(file_name)
    if "-f" not in terminal_command:
        dirs = terminal_command[(terminal_command.index("-d") + 1):]
        create_dirs(dirs)
    if "-d" in terminal_command and "-f" in terminal_command:
        file_name = terminal_command[terminal_command.index("-f") + 1]
        if terminal_command.index("-d") > terminal_command.index("-f"):
            dirs = terminal_command[
                (terminal_command.index("-d") + 1):]
        else:
            dirs = terminal_command[
                (terminal_command.index("-d") + 1):terminal_command.index("-f")
            ]
        create_file(create_dirs(dirs), file_name)


if __name__ == "__main__":
    full_creation()
