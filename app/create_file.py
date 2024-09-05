import sys
import os
from datetime import datetime


def create_file() -> None:
    directory_path = sys.argv
    if "-d" in directory_path and "-f" in directory_path:
        directory = directory_path[directory_path.index("-d") + 1:
                                   directory_path.index("-f")]
        os.makedirs(os.path.join(*directory))
        with open(
            f"{directory}/{directory_path[directory_path.index('-f')]}", "a"
        ) as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            content = input("Enter content line: ")
            line_number = 1
            while content != "stop":
                file.write(f"{line_number} {content}\n")
                content = input("Enter content line: ")
                line_number += 1
    elif "-d" in directory_path:
        directory = directory_path[directory_path.index("-d") + 1:]
        os.makedirs(os.path.join(*directory))
    elif "-f" in directory_path:
        file_name = directory_path[directory_path.index("-f") + 1]
        with open(file_name, "a") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            content = input("Enter content line: ")
            line_number = 1
            while content != "stop":
                file.write(f"{line_number} {content}\n")
                content = input("Enter content line: ")
                line_number += 1
