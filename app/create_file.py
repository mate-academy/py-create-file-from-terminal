import os
import sys
from datetime import datetime


def write_file(file_path: str) -> None:
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(current_time + "\n")

        line_number = 1

        while True:
            current = input("Enter content line: ")

            if current == "stop":
                break

            file.write(f"{line_number} {current}\n")
            line_number += 1


args = sys.argv[1:]

directory_path = ""
file_name = None

if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")

        if d_index < f_index:
            directories = args[d_index + 1:f_index]
        else:
            directories = args[d_index + 1:]
    else:
        directories = args[d_index + 1:]

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

    if directory_path:
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = file_name

    write_file(file_path)
