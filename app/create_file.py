import sys

import os

import datetime

command = sys.argv


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def make_dirs(way: str) -> None:
    os.makedirs(way, exist_ok=True)


def create_and_write_in_file(file_name: str) -> None:
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a") as file:
        file.write(f"{formatted_datetime}\n")
        number_of_line = 1

        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break

            file.write(f"{number_of_line} {text}\n")
            number_of_line += 1

        file.write("\n")


def create_file() -> None:
    if "-d" == command[1] and "-f" == command[4]:
        way_to_file = create_path(command[2:-2])
        make_dirs(way_to_file)

        path_to_create_file = create_path([way_to_file, command[-1]])
        create_and_write_in_file(path_to_create_file)

    if "-d" in command and "-f" not in command:
        way_to_file = create_path(command[2:])
        make_dirs(way_to_file)

    if "-f" in command and "-d" not in command:
        file_name = command[2]
        create_and_write_in_file(os.path.abspath(file_name))


if __name__ == "__main__":
    create_file()
