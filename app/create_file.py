import os
import argparse
from datetime import datetime
from sys import argv


def create_directory(directory_path: str) -> None:
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path)


def create_file_with_user_input(file_path: str) -> None:
    with open(file_path, "a") as file:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{formatted_time}\n")
        line_number = 1

        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {user_input}\n")
            line_number += 1


def process_command_line_args(args: list) -> None:
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-d", nargs="+")
    argument_parser.add_argument("-f")
    parsed_arguments = argument_parser.parse_args()

    if "-d" in args and "-f" in args:
        target_directory_path = os.path.join(
            current_script_dir,
            *parsed_arguments.d
        )
        create_directory(target_directory_path)

        file_path = os.path.join(
            target_directory_path,
            parsed_arguments.f
        )
        create_file_with_user_input(file_path)

    elif "-d" in args:
        target_directory_path = os.path.join(
            current_script_dir,
            *parsed_arguments.d
        )
        create_directory(target_directory_path)

    elif "-f" in args:
        target_file_path = os.path.join(
            current_script_dir,
            parsed_arguments.f
        )
        create_file_with_user_input(target_file_path)


command_from_terminal = argv
process_command_line_args(command_from_terminal)
