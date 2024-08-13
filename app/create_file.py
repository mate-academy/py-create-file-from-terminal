import sys
import os
import datetime


def parsed_command() -> tuple[str, list]:
    full_command = sys.argv
    return full_command[1], full_command[2:]


def create_file(
        name_of_the_file: str,
        create_in_directory: list = None
) -> None | Exception:

    first_line = datetime.datetime.now()

    if create_in_directory:
        create_in_directory.append(name_of_the_file)
        name_of_the_file = os.path.join(*create_in_directory)

    try:
        with open(name_of_the_file, "a") as creating_file:
            creating_file.write(first_line.strftime("%Y-%m-%d %H:%M:%S\n"))
    except Exception as e_info:
        return e_info

    line_num = 1
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break

        try:
            with open(name_of_the_file, "a") as editing_file:
                editing_file.write(f"{line_num} {content}\n")
                line_num += 1
        except Exception as e_info:
            return e_info


def create_directory(path_to_implement: list) -> None:
    try:
        path = os.path.join(*path_to_implement)
        os.makedirs(path, exist_ok=True)
    except OSError as error_info:
        print(error_info)


command, another_part_of_command = parsed_command()

if command == "-f":
    create_file(another_part_of_command[0])

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
    else:
        print("Invalid command")
