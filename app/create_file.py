import os
import sys
from datetime import datetime


def create_directory(console_data: list[str]) -> None:
    dir_index = console_data.index("-d") + 1
    parent_dir = console_data[dir_index]
    dir_names = console_data[dir_index + 1:]

    path = os.path.join(parent_dir, *dir_names)
    os.makedirs(path, exist_ok=True)


def create_file(console_data: list[str]) -> None:
    if "-d" in console_data:
        dir_index = console_data.index("-d") + 1
        parent_dir = console_data[dir_index]
        dir_names = console_data[dir_index + 1: console_data.index("-f")]

        file_index = console_data.index("-f") + 1
        file_name = console_data[file_index]
        file_path = os.path.join(parent_dir, *dir_names, file_name)
    else:
        file_index = console_data.index("-f") + 1
        file_path = console_data[file_index]

    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        counter = 0

        while True:
            message = input("Enter content line: ")
            counter += 1
            if message == "stop":
                break
            file.write(f"{counter} {message}\n")
        file.write("\n")


if __name__ == "__main__":
    console_data = sys.argv

    if "-d" in console_data:
        create_directory(console_data)

    if "-f" in console_data:
        create_file(console_data)
