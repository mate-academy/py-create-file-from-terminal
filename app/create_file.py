import datetime
import os
from sys import argv


file_path = argv[1:]


def make_str_directory(dir_list: list[str]) -> str:
    return os.path.join(*dir_list)


def make_final_directory(dir_str: str) -> None:
    os.makedirs(dir_str, exist_ok=True)


if "-f" not in file_path:
    dir_str = make_str_directory(file_path[1:])
    make_final_directory(dir_str)
    file_dir = None
elif "-d" not in file_path:
    file_dir = file_path[-1]
else:
    for i, arg in enumerate(file_path):
        if arg == "-f":
            file_name = file_path[i + 1]
            break
    not_dir = ["-f", "-d", file_name]
    dir_list = [part for part in file_path if part not in not_dir]
    dir_str = make_str_directory(dir_list)
    make_final_directory(dir_str)
    file_dir = os.path.join(dir_str, file_name)


if file_dir is not None:
    with open(file_dir, "a") as file:
        if os.path.getsize(file_dir) > 0:
            file.write("\n")
        time_now = datetime.datetime.now()
        file.write(f"{time_now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        text = input("Enter content line: ")
        str_num = 1
        while text != "stop":
            file.write(f"{str_num} {text}\n")
            str_num += 1
            text = input("Enter content line: ")
