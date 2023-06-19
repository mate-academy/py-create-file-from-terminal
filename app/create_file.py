import sys
import os
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    content = []

    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.readlines()

    line_number = len(content) + 1
    new_line = input("Enter content line: ")
    while new_line != "stop":
        content.append(f"{line_number} {new_line}\n")
        line_number += 1
        new_line = input("Enter content line: ")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content.insert(0, timestamp + "\n")

    # Write content to file
    with open(filename, "w") as file:
        file.writelines(content)

    print("File created successfully.")


def create_directory(directory: str) -> None:
    os.makedirs(directory)
    print("Directory created successfully.")


def file() -> None:
    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[directory_index:])
        create_directory(directory)

    if "-f" in sys.argv:
        filename_index = sys.argv.index("-f") + 1
        filename = sys.argv[filename_index]
        create_file(directory, filename)


if __name__ == "__main__":
    file()