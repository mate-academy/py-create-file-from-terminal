import sys
import os
from datetime import datetime


def create_file(filename: str) -> None:
    content = []

    if os.path.exists(filename):
        with open(filename, "a") as file:
            file.writelines(content)

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


def create_directory(directory: str) -> None:
    os.makedirs(directory)
    print("Directory created successfully.")


def run_app() -> None:
    if "-d" in sys.argv:
        directory_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[directory_index:])
        create_directory(directory)

    path = ""
    if "-f" in sys.argv:
        file_index = sys.argv.index("-f")
        file_name = sys.argv[file_index + 1]
        file_path = os.path.join(path, file_name)
        create_directory(file_path)


if __name__ == "__main__":
    run_app()
