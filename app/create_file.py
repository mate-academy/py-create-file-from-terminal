import os
from datetime import datetime
from typing import List


class InvalidCommandError(Exception):
    pass


def collecting_user_input(file_name: str, file_path: str) -> None:
    if os.path.getsize(file_path) > 0:
        file_name.write("\n")
    current_date = datetime.now()
    file_name.write(current_date.strftime("%Y-%m-%d % %H:%M:%S"))
    lines_list = []
    while True:
        input_lines = input("Enter content line: ")
        if input_lines == "stop":
            break
        lines_list.append(input_lines)

    for i in range(len(lines_list)):
        file_name.writelines("\n")
        file_name.writelines(str(i + 1))
        file_name.writelines(" ")
        file_name.writelines(lines_list[i])
    file_name.write("\n")


def make_file(file_path: str) -> None:
    try:
        with open(file_path, "a") as new_file:
            collecting_user_input(new_file, file_path)
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
    entered_command = input()
    entered_command = entered_command.strip()
    entered_command = entered_command.split()
    parsing_args(entered_command)
