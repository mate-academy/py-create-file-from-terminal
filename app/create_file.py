import sys
import os
from datetime import datetime


def create_directory_path(path: str):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_name: str):
    with open(file_name, "a") as f:
        current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(current_timestamp + "\n")
        line_number = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line != "stop":
                f.write(f"{line_number} {content_line}\n")
                line_number += 1
            else:
                f.write("\n")
                exit()


def create_file_from_terminal():
    terminal = sys.argv
    if "-d" in terminal and "-f" in terminal:
        path = "/".join(terminal[2:-2])
        create_directory_path(path)
        create_file(f"{path}/{terminal[-1]}")
    elif "-d" in terminal:
        create_directory_path("/".join(terminal[2:-2]))
    elif "-f" in terminal:
        create_file(terminal[-1])
