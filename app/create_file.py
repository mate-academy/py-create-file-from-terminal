import sys
import os
from datetime import datetime


def command_realization() -> None:
    command = sys.argv[1:]

    if "-d" in command and "-f" in command:
        file_name = command.pop(command.index("-f") + 1)
        command.pop(command.index("-f"))
        path = command[command.index("-d") + 1:]
        create_dir_and_file(path, file_name)

    elif "-d" in command:
        command_directory, *path = command

        create_directories(path)

    elif "-f" in command:
        command_file, file_name = command
        create_file(file_name)


def create_directories(path: tuple) -> str:
    path = os.path.join(*path)

    os.makedirs(path, exist_ok=True)

    return path


def create_file(file_name: str) -> None:

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_number = 0
    content_list = []
    user_content = ""

    while user_content.lower() != "stop":
        line_number += 1
        user_content = input("Enter content line:")
        content_list.append(f"{line_number} {user_content}\n")

    with open(file_name, "a") as user_input:
        user_input.write(f"{current_date}\n")
        user_input.write("".join(content_list))


def create_dir_and_file(path: tuple, file_name: str) -> None:
    file_name = os.path.join(create_directories(path), file_name)
    create_file(file_name)


if __name__ == "__main__":
    command_realization()
