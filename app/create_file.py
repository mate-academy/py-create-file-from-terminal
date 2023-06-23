import argparse
import os
from datetime import datetime


def create_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_name: str) -> None:
    data = "\n"
    index = 1
    while True:
        enter = input("Enter content line: ")
        if enter == "stop":
            data += "\n"
            break
        data += f"{index} {enter} \n"
        index += 1
    with open(file_name, "a") as file:
        now = datetime.now()
        file.writelines(now.strftime("%Y-%m-%d %H:%M:%S"))
        file.writelines(data)


def working_with_command(command: argparse.Namespace) -> None:
    if command.file:
        if command.directory:
            dirs = command.directory
            path = os.path.join(*dirs)
            create_dir(path)
            file_name = command.file
            path = os.path.join(path, file_name)
            create_file(path)
        else:
            create_file(command.file)

    if command.directory:
        path = os.path.join(*command.directory)
        create_dir(path)


def read_command() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Create a file")
    parser.add_argument("-d",
                        "--directory",
                        nargs="+",
                        help="Create a directory")

    args = parser.parse_args()
    working_with_command(args)


read_command()
