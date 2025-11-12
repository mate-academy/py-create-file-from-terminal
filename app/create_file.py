import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        while True:
            user_prompt = input("Enter content line: ")
            if user_prompt.strip().lower() == "stop":
                break
            file.write(f"{line_number} {user_prompt}\n")
            line_number += 1


args = sys.argv[1:]

flag_d_index = args.index("-d") if "-d" in args else None
flag_f_index = args.index("-f") if "-f" in args else None


if flag_d_index is not None:
    path_parts = []
    for arg in args[flag_d_index + 1 :]:
        if arg.startswith("-"):
            break
        path_parts.append(arg)

    path = os.path.join(*path_parts)
    create_directory(path)
else:
    path = ""

if flag_f_index is not None:
    file_name = args[flag_f_index + 1]
    full_path = os.path.join(path, file_name) if path else file_name
    create_file(full_path)
