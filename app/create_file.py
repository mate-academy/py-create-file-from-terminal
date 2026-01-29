import os
import sys
from datetime import datetime
from typing import List


class InvalidCommandError(Exception):
    pass


def collecting_user_input(file_name: str) -> None:
    current_date = datetime.now()
    file_name.write(current_date.strftime("%Y-%m-%d %H:%M:%S"))

    lines_list = []
    while True:
        input_lines = input("Enter content line: ")
        if input_lines.lower() == "stop":
            break
        lines_list.append(f"{len(lines_list) + 1} {input_lines}")

    file_name.writelines("\n" + "\n".join(lines_list) + "\n" + "\n")


def make_file(file_path: str) -> None:
    try:
        with open(file_path, "a") as new_file:
            collecting_user_input(new_file)
    except Exception:
        print("Invalid file path")


def parsing_args(entered_command: List[str]) -> None:
    dirs = ""

    if "-d" in entered_command:
        index_d = entered_command.index("-d")
        dirs = os.path.join(
            *entered_command[
                index_d + 1: entered_command.index("-f")
                if "-f" in entered_command else None
            ]
        )
        os.makedirs(dirs, exist_ok=True)

    if "-f" in entered_command:
        index_f = entered_command.index("-f")
        file_name = entered_command[index_f + 1]
        if len(dirs) != 0:
            file_name = os.path.join(dirs, file_name)
        make_file(file_name)

    if "-d" not in entered_command and "-f" not in entered_command:
        raise InvalidCommandError("Invalid command specified")


def create_file() -> None:
    entered_command = sys.argv
    parsing_args(entered_command)
