import argparse
import os
from datetime import datetime


def create_directory(dir_name: str) -> str:
    path = ""

    for directory in dir_name:
        path = os.path.join(path, directory)
        os.mkdir(path)
    return path


def create_file(file_name: str, dir_name: str = "") -> None:
    now = datetime.now()
    new_line = input("Enter new line of content: ")
    n = 0

    if os.path.exists(file_name):
        with open(file_name, "a") as file:
            file.write(f"\n")

    with open(os.path.join(create_directory(dir_name), file_name), "a") as file:
        file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n")

        while new_line != "stop":
            n += 1
            file.write(f"{n} {new_line}\n")
            new_line = input("Enter new line of content: ")


def creating_with_terminal() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help="create new file")
    parser.add_argument('-d', nargs="*", help="create new directory")
    args = parser.parse_args()
    file_name = args.f
    directory_name = args.d

    if args.d and args.f:
        create_file(file_name, directory_name)

    elif args.f:
        create_file(file_name)

    elif args.d:
        create_directory(directory_name)


creating_with_terminal()




