import sys
import os
from datetime import datetime


def create_directory(directory: list) -> None:
    directory = os.path.join(*directory)
    os.makedirs(directory, exist_ok=True)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        if os.path.exists(file_path):
            f.write("\n")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{current_time}\n")

        line_number = 1

        while True:
            line_number += 1
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            f.write(f"{line_number} {line}\n")


def main() -> None:
    flag = sys.argv[1]

    if flag == "-d" and "-f" not in sys.argv:
        create_directory(sys.argv[2:])
    elif flag == "-d" and "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        directory_parts = sys.argv[2:f_index]
        create_directory(directory_parts)

        file_name = sys.argv[f_index + 1]
        file_path = os.path.join(*directory_parts, file_name)
        create_file(file_path)
