import os
import sys
from datetime import datetime


def directory_maker(dirs: list) -> str:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def file_creator(*args) -> None:
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


def total_creation() -> None:
    terminal_command = sys.argv
    if "-d" not in terminal_command and "-f" in terminal_command:
        file_name = terminal_command[terminal_command.index("-f") + 1]
        file_creator(file_name)
    if "-f" not in terminal_command and "-d" in terminal_command:
        dirs = terminal_command[(terminal_command.index("-d") + 1):]
        directory_maker(dirs)
    if "-d" in terminal_command and "-f" in terminal_command:
        file_name = terminal_command[terminal_command.index("-f") + 1]
        if terminal_command.index("-d") > terminal_command.index("-f"):
            dirs = terminal_command[
                (terminal_command.index("-d") + 1):]
        else:
            dirs = terminal_command[
                (terminal_command.index("-d") + 1):terminal_command.index("-f")
            ]
        file_creator(directory_maker(dirs), file_name)


if __name__ == "__main__":
    total_creation()
