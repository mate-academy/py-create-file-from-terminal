import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    current_directory = os.path.dirname(__file__)
    path = os.path.join(current_directory, *directories)
    os.makedirs(path)
    return path


def create_file_with_content_from_input(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.writelines(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

        line_number = 0

        while True:
            file_line = input("Enter content line: ")
            if file_line == "stop":
                file.writelines("\n")
                break
            line_number += 1
            file.writelines(f"{line_number} {file_line}\n")


def create_file_from_terminal() -> None:
    terminal_input = sys.argv
    current_directory = os.path.dirname(__file__)

    if terminal_input[1] == "-f":
        file_name = terminal_input[2]
        file_path = os.path.join(current_directory, file_name)
        create_file_with_content_from_input(file_path)

    try:

        if terminal_input[1] == "-d" and "-f" not in terminal_input:
            directories_list = terminal_input[2:]
            create_path(directories_list)

        if "-d" in terminal_input and "-f" in terminal_input:
            directories_list = terminal_input[2:terminal_input.index("-f")]
            file_name = terminal_input[-1]
            file_path = os.path.join(
                create_path(directories_list),
                file_name
            )
            create_file_with_content_from_input(file_path)

    except FileExistsError:
        print("Such directories already exists")


if __name__ == "__main__":
    create_file_from_terminal()
