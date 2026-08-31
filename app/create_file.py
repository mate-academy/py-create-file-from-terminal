import sys
import os
import datetime


def create_path(path_list: list) -> str:
    if "-d" in path_list:
        d_index = path_list.index("-d")
        if "-f" in path_list:
            f_index = path_list.index("-f")
            if d_index < f_index:
                directories = path_list[d_index + 1 : f_index]
            else:
                directories = path_list[d_index + 1 :]
        else:
            directories = path_list[d_index + 1 :]
        return os.path.join(*directories) if directories else "."
    return "."


def create_filename(path_list: list) -> str:
    if "-f" in path_list:
        f_index = path_list.index("-f")
        if f_index + 1 < len(path_list):
            return path_list[f_index + 1]
    return "file.txt"


def make_dir(user_path: str | bytes) -> None:
    if user_path and user_path != ".":
        os.makedirs(user_path, exist_ok=True)


def create_file(user_path: str | bytes, filename: str) -> None:
    file_path = os.path.join(user_path, filename)
    is_not_empty = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a") as target_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if is_not_empty:
            target_file.write(f"\n{timestamp}\n")
        else:
            target_file.write(f"{timestamp}\n")
        line_number = 1
        while True:
            try:
                user_prompt = input("Enter content line: ")
            except (EOFError, KeyboardInterrupt, OSError):
                break
            if user_prompt == "stop":
                break
            target_file.write(f"{line_number} {user_prompt}\n")
            line_number += 1


user_commands = sys.argv[1:]
path_to_create = create_path(user_commands)
file_name = create_filename(user_commands)
make_dir(path_to_create)
create_file(path_to_create, file_name)
