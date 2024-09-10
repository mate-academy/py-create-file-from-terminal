import sys
import os
from datetime import datetime


directory_path = sys.argv


def create_file_and_directory() -> None:
    if ("-d" in directory_path
            and "-f" in directory_path
            and directory_path.index("-d") < directory_path.index("-f")):
        directory = directory_path[directory_path.index("-d") + 1:
                                   directory_path.index("-f")]
        os.makedirs(os.path.join(*directory), exist_ok=True)
        create_file(directory)
    elif ("-d" in directory_path
          and "-f" in directory_path
          and directory_path.index("-f") < directory_path.index("-d")):
        directory = directory_path[directory_path.index("-d") + 1:]
        os.makedirs(os.path.join(*directory), exist_ok=True)
        create_file(directory)
    elif "-d" in directory_path:
        directory = directory_path[directory_path.index("-d") + 1:]
        os.makedirs(os.path.join(*directory), exist_ok=True)
    elif "-f" in directory_path:
        create_file([])


def create_file(directory: list) -> None:
    file_name = directory_path[directory_path.index("-f") + 1]
    file_path = os.path.join(*directory, file_name)
    with open(file_path, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        content = input("Enter content line: ")
        line_number = 1
        while content != "stop":
            file.write(f"{line_number} {content}\n")
            content = input("Enter content line: ")
            line_number += 1


create_file_and_directory()
