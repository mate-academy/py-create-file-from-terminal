import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    current_directory = os.path.dirname(__file__)
    path = os.path.join(current_directory, *directories)
    os.makedirs(path, exist_ok=True)
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
    command_length = len(terminal_input)

    if command_length > 2:
        directories_list = []

        if terminal_input[1] == "-d":
            for item in range(2, len(terminal_input)):
                if terminal_input[item] == "-f":
                    break
                directories_list.append(terminal_input[item])
            create_path(directories_list)

        for i in range(1, command_length):
            if terminal_input[i] == "-f":
                file_name = terminal_input[i + 1]

                file_path = os.path.join(
                    current_directory,
                    create_path(directories_list),
                    file_name
                )

                create_file_with_content_from_input(file_path)


if __name__ == "__main__":
    create_file_from_terminal()
