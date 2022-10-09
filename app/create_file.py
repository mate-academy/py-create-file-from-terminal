import os

import sys

from datetime import datetime


def main() -> None:
    get_path_create_directory_and_file()


def create_a_file(file_name: str) -> None:
    with open(file_name, "a") as file_out:
        line_number = 1
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_out.write(f"{time_stamp}\n")
        user_input = input("Enter content line: ")

        while user_input.lower() != "stop":
            file_out.write(f"{line_number} {user_input}\n")
            line_number += 1
            user_input = input("Enter content line: ")

        file_out.write("\n")


def new_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True) if path else None


def get_path_create_directory_and_file() -> None:
    command = sys.argv

    if "-f" in command:
        file_name = command[-1]
        if "-d" in command:
            index_f = command.index("-f")
            index_d = command.index("-d")
            path = "/".join(command[(index_d + 1): index_f])
            new_directory(path)
            file_name = "/".join([path, file_name])
            create_a_file(file_name)
        create_a_file(file_name)
        if "-d" in command:
            index_d = command.index("-d")
            path = "/".join(command[(index_d + 1):])
            new_directory(path)


if __name__ == "__main__":
    main()
