import os
from datetime import datetime
from sys import argv


def create_directory(directory_path: str) -> None:
    if not os.path.isdir(directory_path):
        os.makedirs(directory_path, exist_ok=True)


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

    if "-d" in args and "-f" in args:
        directory_args = [
            args[x] for x in range(args.index("-d") + 1, args.index("-f"))
        ]
        target_directory_path = os.path.join(
            current_script_dir,
            *directory_args
        )
        create_directory(target_directory_path)

        file_name = args[-1]
        file_path = os.path.join(target_directory_path, file_name)
        create_file_with_user_input(file_path)

    elif "-d" in args:
        directory_args = [
            args[x] for x in range(args.index("-d") + 1, len(args))
        ]
        target_directory_path = os.path.join(
            current_script_dir,
            *directory_args
        )
        create_directory(target_directory_path)

    elif "-f" in args:
        file_name = args[2]
        target_file_path = os.path.join(current_script_dir, file_name)
        create_file_with_user_input(target_file_path)


command_from_terminal = argv
process_command_line_args(command_from_terminal)
