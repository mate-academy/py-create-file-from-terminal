import sys

import os

import datetime


def get_command() -> None:
    if "-d" in command and "-f" not in command:
        path_dest = os.path.join(*command[command.index("-d") + 1 :])
        create_directory(path_dest)
    elif "-d" in command and "-f" in command:
        index_d = command.index("-d")
        index_f = command.index("-f")

        path_dest = os.path.join(*command[index_d + 1 : index_f])
        create_directory(path_dest)

        create_file(path_dest, command[index_f + 1])
    elif "-f" in command and "-d" not in command:
        create_file("", command[command.index("-f") + 1])


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(path: str, file_name: str) -> None:
    path = os.path.join(path, file_name)
    mode = "a" if os.path.exists(path) else "w"
    write_to_file(path, mode)


def write_to_file(path_file: str, mode: str) -> None:
    with open(path_file, mode) as file:
        file.write(
            f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
        )
        line_number = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(f"{line_number} {text}\n")
            line_number += 1


command = sys.argv
if __name__ == "__main__":
    get_command()
