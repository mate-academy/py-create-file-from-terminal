from os import path, makedirs
from datetime import datetime
import sys


def create_path(dirs: tuple) -> str:
    directory_path = path.join(*dirs)
    makedirs(directory_path, exist_ok=True)
    return directory_path


def get_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_file(directory_path: str, file_name: str) -> None:
    file_path = path.join(directory_path, file_name)
    with open(file_path, "a") as file:
        time = get_time()
        file.write(time + "\n")
        line = input("Enter content line: ")
        while line != "stop":
            line = input("Enter content line: ")
            file.write(line + "\n")


def main() -> callable:

    if "-d" in sys.argv and "-f" in sys.argv:
        current_dir, command_b, *dirs, command_f, file_name = sys.argv
        return create_file(create_path(dirs), file_name)
    elif "-d" in sys.argv:
        current_dir, command, *dirs = sys.argv
        return create_path(dirs)
    elif "-f" in sys.argv:
        current_dir, command, file_name = sys.argv
        return create_file(".", file_name)
