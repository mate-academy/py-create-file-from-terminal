import os
import sys
from datetime import datetime


def get_file_path(args: list) -> None:
    file_name = None
    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    dirs = []
    if "-d" in args:
        d_index = args.index("-d")
        for item in args[d_index + 1:]:
            if item.startswith("-"):
                break
            dirs.append(item)

    file_path = file_name

    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
        if file_name:
            file_path = os.path.join(dir_path, file_name)

    return file_path


def write_content_to_file(file_path: str) -> str:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n")
        f.write(f"{current_time}\n")

        line_number = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            f.write(f"{line_number} {user_input}\n")
            line_number += 1


arguments = sys.argv
final_path = get_file_path(arguments)

if final_path:
    write_content_to_file(final_path)
