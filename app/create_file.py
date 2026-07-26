import os
import sys
from datetime import datetime


def create_path(directories_list: list) -> str:
    path = os.path.join(*directories_list)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file_pointer:
        file_pointer.write(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n"
        )
        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file_pointer.write(f"{line} {content} \n")
            line += 1


def process_command_line(command_line: list[str]) -> None:
    if (
        "-d" not in command_line
        and "-f" not in command_line
        or len(command_line) <= 2
    ):
        print(
            "Please provide correct command: "
            "python create_file.py -f <filename> and/or -d <dir>"
        )
        sys.exit(1)

    if "-d" in command_line and "-f" in command_line:
        _, command_d, *directories, command_f, file_name = command_line
        path = create_path(directories)
        file_path = f"{path}/{file_name}"
        create_file(file_path)

    elif "-d" in command_line:
        _, command_d, *directories = command_line
        create_path(directories)

    elif "-f" in command_line:
        _, command_f, file_name = command_line
        create_file(file_name)


if __name__ == "__main__":
    command_line = sys.argv
    process_command_line(command_line)
