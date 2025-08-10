import sys
import os
import datetime


def make_dirs_and_return_path(argv: list[str]) -> str:
    dirs_path = ""
    for dir_index in range(1, len(argv)):
        if argv[dir_index] == "-f":
            break
        dirs_path += argv[dir_index] + "/"

    os.makedirs(dirs_path, exist_ok=True)
    return dirs_path


def make_file(dirs_path: str, file_name: str) -> str:
    absolute_file_name = dirs_path + file_name
    with open(absolute_file_name, "a") as file:
        file.write(datetime.datetime.now()
                   .strftime("%Y-%m-%d %H:%M:%S") + "\n")

    return absolute_file_name


def write_data_into_file_if_exist(has_file: bool, file_name: str) -> None:
    i = 0
    while has_file:
        expected_input = input("Enter content line: ")
        if expected_input == "stop":
            with open(file_name, "a") as file:
                file.write("\n")
            break

        i += 1
        with open(file_name, "a") as file:
            file.write(f"{i} {expected_input}\n")


def create_file(argv: list[str]) -> None:
    has_file = False
    file_name = ""
    dirs_path = ""
    for i in range(len(argv)):
        if argv[i] == "-d":
            dirs_path = make_dirs_and_return_path(argv)

        if argv[i] == "-f":
            file_name = make_file(dirs_path, argv[i + 1])
            has_file = True

    write_data_into_file_if_exist(has_file, file_name)


create_file(sys.argv[1:])
