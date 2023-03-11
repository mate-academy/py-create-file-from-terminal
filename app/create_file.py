import os
from datetime import datetime
import argparse


def create_path(directories: list[str]) -> str:
    return os.path.join(*directories)


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def content_input(path: str) -> None:
    with open(path, "a") as file:
        line_counter = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{line_counter} {line}\n")
            line_counter += 1


def add_timestamp(path: str) -> None:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as file:
        file.write(f"{timestamp}\n")


terminal_parser = argparse.ArgumentParser()
terminal_parser.add_argument(
    "-d", dest="directories", type=str, nargs="*", metavar="directories names",
    help="creates directories inside current directory"
)
terminal_parser.add_argument(
    "-f", dest="file_name", type=str, nargs=1, metavar="file name",
    help="create file and input content lines until 'stop'"
)
argument_in_terminal = terminal_parser.parse_args()

current_working_directory = os.getcwd()

if argument_in_terminal.directories:
    current_working_directory = create_path(argument_in_terminal.directories)
    create_directory(current_working_directory)

if argument_in_terminal.file_name:
    path_to_file = [
        current_working_directory, argument_in_terminal.file_name[0]
    ]
    path = create_path(path_to_file)
    add_timestamp(path)
    content_input(path)
