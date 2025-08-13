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
            if user_input != "stop":
                file.write(f"{counter} {user_input}\n")
                counter += 1


def create_file() -> None:
    args = sys.argv
    directory_path = None
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        # If -f exists, stop before it; otherwise take all remaining args
        end_index = args.index("-f") if "-f" in args else len(args)
        directory_parts = args[d_index + 1:end_index]
        if directory_parts:
            directory_path = os.path.join(*directory_parts)
            os.makedirs(directory_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 >= len(args):
            print("Error: Missing file name after -f")
            return
        file_name = args[f_index + 1]
        # Create file path based on whether -d was provided
        file_path = (os.path.join(directory_path, file_name)
                     if directory_path else file_name)
        write_file(file_path)

    if "-d" not in args and "-f" not in args:
        print("Error, need additional arguments")
