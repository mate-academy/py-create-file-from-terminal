import sys
import os
from datetime import datetime


def get_directory(command: list) -> str:
    if "-d" in command and "-f" in command:
        flag_d = command.index("-d")
        flag_f = command.index("-f")
        if flag_d < flag_f:
            path = os.path.join(*command[(flag_d + 1):flag_f])
            os.makedirs(path, exist_ok=True)
            file_name = command[flag_f + 1]
        else:
            path = os.path.join(*command[(flag_d + 1):])
            os.makedirs(path, exist_ok=True)
            file_name = command[flag_f + 1]
        return os.path.join(path, file_name)

    if "-d" in command:
        flag = command.index("-d")
        path = os.path.join(
            *command[(flag + 1):]
        )
        os.makedirs(path, exist_ok=True)

    if "-f" in command:
        flag_f = command.index("-f")
        file_name = command[flag_f + 1]

        return file_name


def create_and_write_file(file_path: str) -> None:
    with open(f"{file_path}", "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S \n"))
        count_line = 0
        while True:
            enter_line = input("Enter content line: ")
            count_line += 1
            if enter_line == "stop":
                break
            file.write(f"{count_line} {enter_line}\n")
        file.write("\n")


def create_file() -> None:
    commands = sys.argv

    file_path = get_directory(commands)

    if file_path is not None:
        create_and_write_file(file_path)


create_file()
