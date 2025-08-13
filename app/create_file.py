# write your code here
import os
import sys
from datetime import datetime


def write_file(file_name: str) -> None:

    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        counter = 1
        user_input = ""
        while user_input.strip().lower() != "stop":
            user_input = input("Enter content line: ")
            if user_input.strip().lower() != "stop":
                file.write(f"{counter} {user_input}\n")
                counter += 1


def create_file() -> None:
    flags = sys.argv

    if "-d" not in flags and "-f" not in flags:
        print("Error, need additional arguments")

    elif "-d" in flags and "-f" not in flags:
        directory_parts = flags[sys.argv.index("-d") + 1:]
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)

    elif "-d" not in flags and "-f" in flags:
        file_name = flags[sys.argv.index("-f") + 1]
        write_file(file_name)

    elif "-d" in flags and "-f" in flags:
        directory_parts = flags[sys.argv.index("-d") + 1: sys.argv.index("-f")]
        directory_path = os.path.join(*directory_parts)
        os.makedirs(directory_path, exist_ok=True)

        file_name = flags[sys.argv.index("-f") + 1]
        full_file_path = os.path.join(directory_path, file_name)
        write_file(full_file_path)
