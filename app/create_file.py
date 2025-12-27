import sys
import os
from datetime import datetime


def create_file_and_directory_from_terminal():
    from_terminal = sys.argv

    if "-d" in from_terminal and "-f" in from_terminal:
        start_of_path = from_terminal[from_terminal.index("-d") + 1]
        end_of_path = from_terminal[1:from_terminal.index("-f")]
        directory_path = from_terminal[start_of_path: end_of_path]
        file_name = os.path.join(
            create_directory(directory_path),
            from_terminal[from_terminal.index("-f") + 1]
        )
        create_file(file_name)

    if "-d" in from_terminal:
        create_directory(from_terminal[2:])

    if "-f" in from_terminal:
        create_file(from_terminal[2])


def create_directory(directory_path):
    path = os.path.join(directory_path)
    if os.path.exists(path) is False:
        os.makedirs(path)
    return path


def create_file(file_name):
    with open("file_name", "w") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        count = 1

        while True:
            content_lines = input("Enter content line: ")
            if content_lines != "stop":
                file.write(f"{count} {content_lines}\n")
                count += 1
            else:
                break
