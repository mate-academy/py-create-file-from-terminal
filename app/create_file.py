import os
from datetime import datetime
from sys import argv


def create_directory(parent_dir: str, child_dir: str) -> None:
    directory_path = os.path.join(parent_dir, child_dir)
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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(script_dir, args[2])

    if "-d" in args and "-f" in args and len(args) == 6:
        create_directory(target_path, args[3])

        file_path = os.path.join(target_path, args[3], args[5])
        create_file_with_user_input(file_path)

    elif "-d" in args and len(args) == 4:
        create_directory(target_path, args[3])

    elif "-f" in args and len(args) == 3:
        create_file_with_user_input(target_path)


command_from_terminal = argv
process_command_line_args(command_from_terminal)
