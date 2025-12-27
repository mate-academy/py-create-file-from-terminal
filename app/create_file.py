import sys
import os
from datetime import datetime


def create_file() -> None:
    if "-d" not in sys.argv:
        file_path = sys.argv[2]
    else:
        file_path = os.path.join(sys.argv[2], sys.argv[3], sys.argv[5])
    with open(file_path, "a+") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %I:%M:%S") + "\n")
        line_number = 1
        while True:
            new_line_of_content = input("Enter content line: ")
            if new_line_of_content.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_number} {new_line_of_content}\n")
            line_number += 1


def create_directory() -> None:
    directory_name = os.path.join(sys.argv[2], sys.argv[3])
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")


if "-f" in sys.argv and "-d" not in sys.argv:
    create_file()

if "-d" in sys.argv and "-f" not in sys.argv:
    create_directory()

if "-f" in sys.argv and "-d" in sys.argv:
    create_directory()
    create_file()
