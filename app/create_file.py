import sys
import datetime
import os

args = sys.argv[1:]

dir_parts = []
file_name = ""

d_index = args.index("-d") if "-d" in args else None
f_index = args.index("-f") if "-f" in args else None

if d_index is not None:
    if f_index is not None and f_index > d_index:
        dir_parts = args[d_index + 1: f_index]
    else:
        dir_parts = args[d_index + 1:]

if f_index is not None:
    file_name = args[f_index + 1]


def create_path(directories: list) -> str:
    if not directories:
        return ""

    path = os.path.join(*directories)
    if path:
        os.makedirs(path, exist_ok=True)
    return path


def write_content_to_file(full_path: str) -> None:
    file_is_here = os.path.exists(full_path)
    has_content = file_is_here and os.path.getsize(full_path) > 0

    with open(full_path, "a") as file:
        if has_content:
            file.write("\n")

        line_number = 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")

        while True:
            user_input = input("Enter content line: ")
            if user_input.lower() == "stop":
                break

            file.write(f"{line_number} {user_input}\n")
            line_number += 1


path_to_folder = create_path(dir_parts)
full_path = os.path.join(path_to_folder, file_name)

if file_name:
    write_content_to_file(full_path)
