import os
import sys
from datetime import datetime


def create_file(directory_path: str, file_name: str) -> None:
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, "a") as file:
        current_datetime = datetime.now()
        file.write(current_datetime.strftime("%Y-%m-%d %H:%M:%S" + "\n"))
        content = input("Enter content line: ")
        while content != "stop":
            file.write(content + "\n")
            content = input("Enter content line: ")


def create_directory(dirs: tuple) -> str:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def main() -> callable:
    command = sys.argv
    if "-d" in command and "-f" in command:
        current_dir, command_b, *dirs, command_f, file_name = command
        return create_file(create_directory(dirs), file_name)
    elif "-d" in command:
        current_dir, command, *dirs = command
        return create_directory(dirs)
    elif "-f" in command:
        current_dir, command, file_name = command
        return create_file(".", file_name)


if __name__ == "__main__":
    main()
