import os
import sys
from datetime import datetime
from typing import IO


def add_new_content_line(new_file: IO) -> None:
    new_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    added_line = ""
    while added_line != "stop":
        added_line = input("Enter content line: ")
        if added_line != "stop":
            new_file.write(f"{added_line}\n")
        else:
            new_file.write("\n")


def create_only_file() -> None:
    if "-f" in sys.argv and "-d" not in sys.argv:
        with open(sys.argv[-1], "a") as created_file:
            add_new_content_line(created_file)


def create_only_folders() -> None:
    if "-d" in sys.argv and "-f" not in sys.argv:
        os.makedirs(os.path.join(*sys.argv[2:]), exist_ok=True)


def create_folders_and_file() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        sys.argv.remove("-f")
        sys.argv.remove("-d")
        os.makedirs(os.path.join(*sys.argv[1:-1]), exist_ok=True)
        with open(os.path.join(*sys.argv[2:]), "a") as created_file:
            add_new_content_line(created_file)


if __name__ == "__main__":
    create_only_file()
    create_only_folders()
    create_folders_and_file()
