import os
import sys
from datetime import datetime

arguments = sys.argv


def create_directory_only(folders: list) -> str:
    path = os.path.join(*folders)
    os.makedirs(path, exist_ok=True)
    return str(path)


def create_file_only(file_name: str) -> None:
    with open(file_name, "a") as file:
        current_date = datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S\n"))
        number_line = 0
        while True:
            file_content = input("Enter content line: ")
            if file_content == "stop":
                break

            number_line += 1
            file.write(f"{number_line} {file_content}\n")
