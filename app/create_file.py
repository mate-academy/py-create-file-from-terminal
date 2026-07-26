from os import path, makedirs
from datetime import datetime
import sys


def create_directory_path(dirs: tuple) -> str:
    directory_path = path.join(*dirs)
    makedirs(directory_path, exist_ok=True)
    return directory_path


def create_file(directory_path: str, file_name: str) -> None:
    file_path = path.join(directory_path, file_name)
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
        line = input("Enter content line: ")
        while line != "stop":
            line = input("Enter content line: ")
            file.write(line + "\n")


def main() -> callable:
    input_commands = sys.argv

    if "-d" in input_commands and "-f" in input_commands:
        current_dir, command_b, *dirs, command_f, file_name = input_commands
        return create_file(create_directory_path(dirs), file_name)
    elif "-d" in input_commands:
        current_dir, command, *dirs = input_commands
        return create_directory_path(dirs)
    elif "-f" in input_commands:
        current_dir, command, file_name = input_commands
        return create_file(".", file_name)


if __name__ == "__main__":
    main()
