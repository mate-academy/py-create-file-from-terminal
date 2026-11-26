import os
from datetime import datetime
from sys import argv

file_path = argv[1:]


def make_str_directory(dir_list: list[str]) -> str:
    return os.path.join(*dir_list)


def make_final_directory(dir_str: str) -> None:
    os.makedirs(dir_str, exist_ok=True)


dir_list = []
file_name = None
file_dir = None
for i, arg in enumerate(file_path):
    if arg == "-f":
        file_name = file_path[i + 1]
        file_dir = file_name
    if arg == "-d":
        for part in file_path[i + 1:]:
            if part != "-f":
                dir_list.append(part)
            else:
                break


if dir_list:
    dir_str = make_str_directory(dir_list)
    make_final_directory(dir_str)
    if file_name is not None:
        file_dir = os.path.join(dir_str, file_name)


if file_dir is not None:
    with open(file_dir, "a") as file:
        if os.path.getsize(file_dir) > 0:
            file.write("\n")
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time_now}\n")
        text = input("Enter content line: ")
        str_num = 1
        while text != "stop":
            file.write(f"{str_num} {text}\n")
            str_num += 1
            text = input("Enter content line: ")
