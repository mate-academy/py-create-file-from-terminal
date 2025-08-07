import os
import sys
from datetime import datetime


def fill_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.strip().lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1
        file.write("\n")


def create_file(args: list) -> None:
    d_index = args.index("-d") if "-d" in args else None
    f_index = args.index("-f") if "-f" in args else None
    if "-d" in args and "-f" in args:
        dir_parts = args[d_index + 1 : f_index]
        filename = args[f_index + 1]
    elif "-d" in args:
        dir_parts = args[d_index + 1 :]
        filename = None
    elif "-f" in args:
        dir_parts = []
        filename = args[f_index + 1]
    else:
        print("Error: No flags provided")
        return

    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."

    if filename:
        file_path = os.path.join(dir_path, filename)
        fill_file(file_path)


if __name__ == "__main__":
    create_file(sys.argv[1:])
