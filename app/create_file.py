import sys
import os
from datetime import datetime


def perform_command() -> None:
    arguments = sys.argv
    path = ""

    if "-d" in arguments:
        dir_start_index = arguments.index("-d") + 1
        path = create_directory(arguments[dir_start_index:])
    if "-f" in arguments:
        file_name_index = arguments.index("-f") + 1
        create_file(path, arguments[file_name_index])


def create_directory(arguments: list[str]) -> str:
    path = ""
    for value in arguments:
        if value == "-f":
            break
        path = os.path.join(path, value)

    try:
        os.makedirs(path)
    except FileExistsError:
        pass
    return path


def create_file(path: str, file_name: str) -> None:
    path = os.path.join(path, file_name)
    with open(path, "a+") as file_out:
        file_out.write(fill_file())


def fill_file() -> str:
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_content = f"{current_date}\n"
    line_number = 0

    while True:
        current_line = input("Enter content line: ")
        if current_line.lower() == "stop":
            break
        line_number += 1
        file_content += f"{line_number} {current_line}\n"

    return f"{file_content}\n"


if __name__ == "__main__":
    perform_command()
