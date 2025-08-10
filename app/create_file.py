import os
import sys
from datetime import datetime


def create_path(path_parts: list) -> str:
    return os.path.join(*path_parts)


def create_directory(directories_path: str) -> None:
    os.makedirs(directories_path, exist_ok=True)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower().strip() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def parse_command_line() -> None:
    command_parts = sys.argv

    if "-d" in command_parts and "-f" not in command_parts:
        directories_path_parts = command_parts[2:]
        directories_path = create_path(directories_path_parts)
        create_directory(directories_path)

    elif "-f" in command_parts and "-d" not in command_parts:
        file_name = command_parts[-1]
        create_file(file_name)

    elif "-d" in command_parts and "-f" in command_parts:
        directories_path_parts = command_parts[2:-2]
        directories_path = create_path(directories_path_parts)
        create_directory(directories_path)

        file_name = command_parts[-1]
        file_path_parts = directories_path_parts + [file_name]
        file_path = create_path(file_path_parts)
        create_file(file_path)


if __name__ == "__main__":
    parse_command_line()
