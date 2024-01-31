import sys

import os

import datetime

command = sys.argv

print("command: ", command)


current_datetime = datetime.datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def make_dir(way: str) -> None:
    if not os.path.exists(way):
        os.makedirs(way)
    else:
        print("Directory already exist!")


def create_and_write_in_file(file_name: str) -> None:

    with open(file_name, "a") as file:
        text = input("Enter content line: ")
        file.write(f"{formatted_datetime}\n")
        number_of_line = 1
        while text != "stop":

            if text != "stop":
                file.write(f"{number_of_line} {text}\n")
            number_of_line += 1
            text = input("Enter content line: ")

        file.write("\n")


if "-d" in command and "-f" in command:
    way_to_file = create_path(command[2:-2])
    make_dir(way_to_file)

    path_to_create_file = way_to_file + "/" + command[-1]
    create_and_write_in_file(path_to_create_file)

if "-d" in command and "-f" not in command:
    way_to_file = create_path(command[2:])
    make_dir(way_to_file)


if "-f" in command and "-d" not in command:
    file_name = command[2]
    create_and_write_in_file(os.path.abspath(file_name))
