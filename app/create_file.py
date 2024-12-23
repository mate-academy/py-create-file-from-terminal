import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    file_name = None
    path = None

    if "-d" in args:
        directory_index = args.index("-d")
        directories = args[directory_index + 1:]
        if "-f" in directories:
            file_index = directories.index("-f")
            directories = directories[:file_index]
            if directory_index + 2 + file_index < len(args):
                file_name = args[directory_index + 2 + file_index]
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)

    if "-f" in args:
        file_index = args.index("-f")
        if file_index + 1 < len(args):
            file_name = args[file_index + 1]
        if path is None:
            path = "."

    if file_name:
        file_path = os.path.join(path, file_name)
        with open(file_path, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp}\n")
            line_number = 1
            while True:
                content_line = input("Enter content line: ")
                if content_line.lower() == "stop":
                    break
                file.write(f"{line_number} {content_line}\n")
                line_number += 1


create_file()
