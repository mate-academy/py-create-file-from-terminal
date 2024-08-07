import sys
import os
import datetime
from typing import Callable


def create_file(
        name_of_the_file: str,
        create_in_directory: list = None
) -> None:

    first_line = datetime.datetime.now()

    if create_in_directory:
        create_in_directory.append(name_of_the_file)
        name_of_the_file = os.path.join(*create_in_directory)

    with open(name_of_the_file, "w") as creating_file:
        creating_file.write(first_line.strftime("%Y-%m-%d %H:%M:%S\n"))
        line_num = 1
        while True:
            content = input("Enter content line: ")
            if len(content) == 0:
                print("Cannot add empty line")
                continue
            if content == "stop":
                break

            creating_file.write(f"{line_num} {content}\n")
            line_num += 1


def create_path(func: Callable) -> Callable:
    def inner(directories: list) -> None:
        path = os.path.join(*directories)
        func(path)

    return inner


@create_path
def create_directory(path_to_implement: str) -> None:
    try:
        os.makedirs(path_to_implement)
    except OSError as error_info:
        print(error_info)


full_command = sys.argv
command, *another_part_of_command = full_command[1:]

if command == "-f":
    create_file(another_part_of_command)

elif command == "-d":
    path_to_create = []

    for directory in another_part_of_command:
        if directory != "-f":
            path_to_create.append(directory)
            continue
        another_part_of_command = (
            another_part_of_command
            [another_part_of_command.index("-f"):]
        )
        break

    create_directory(path_to_create)

    if len(another_part_of_command) != 0:
        command, file_to_create = another_part_of_command
        if command == "-f":
            create_file(file_to_create, path_to_create)
