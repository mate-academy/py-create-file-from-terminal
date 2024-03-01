import sys
import os
from datetime import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 0
        while True:
            user_text = input("Enter content line: ")
            if user_text.lower() == "stop":
                break
            line_number += 1
            file.write(f"{line_number} {user_text} \n")


def create_directory(path: list) -> None:
    os.makedirs(os.path.join(*path[1:]), exist_ok=True)


def create_file_with_path(command: list) -> None:
    path = command[:-2]
    create_directory(path)

    command.remove("-d")
    command.remove("-f")
    file_name = os.path.join(*command)
    create_file(str(file_name))


input_command = sys.argv[1:]

if input_command[0] == "-f":
    if input_command.count("-d"):
        input_command = input_command[2:] + input_command[:2]
    else:
        create_file(input_command[-1])

if input_command[0] == "-d":
    if input_command.count("-f"):
        create_file_with_path(input_command)
    else:
        create_directory(input_command)
