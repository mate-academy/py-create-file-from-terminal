import os
import sys

from datetime import datetime
from os import path, makedirs
from typing import IO


def main() -> None:

    if "-d" in sys.argv and "-f" in sys.argv:
        if len(sys.argv) < 5:
            print("Usage: python script.py -d <directory> -f <file_name>")
            return
        working_file, command_d, *dirs, command_f, file_name = sys.argv
        create_file(create_path(dirs), file_name)
    elif "-d" in sys.argv:
        if len(sys.argv) < 3:
            print("Usage: python script.py -d <directory>")
            return
        working_file, command, *dirs = sys.argv
        create_path(dirs)
    elif "-f" in sys.argv:
        if len(sys.argv) < 3:
            print("Usage: python script.py -f <file_name>")
            return
        working_file, command, file_name = sys.argv
        create_file(".", file_name)


def create_path(dirs: tuple) -> str:
    directory_path = path.join(*dirs)
    makedirs(directory_path, exist_ok=True)
    return directory_path


def write_file(file_handle: IO, counter: int) -> None:
    text = input("Enter content line: ")
    while text != "stop":
        file_handle.write(f"\n{counter} {text}")
        counter += 1
        text = input("Enter content line: ")


def create_file(directory_path: str, file_name: str) -> None:
    counter = 1
    file_create = path.join(directory_path, file_name)
    if os.path.exists(file_create):
        with open(file_create, "a") as file:
            file.write(f"\n\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            write_file(file, counter)
    else:
        with open(file_create, "w") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            write_file(file, counter)


if __name__ == "__main__":
    main()
