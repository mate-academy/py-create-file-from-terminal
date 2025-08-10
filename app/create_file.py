import os
import sys
from _datetime import datetime


def create_path(data_list: list) -> str:
    full_path = os.path.join(".", *data_list)
    try:
        os.makedirs(full_path)
    except FileExistsError:
        pass
    return full_path


def create_file(name: str, path: str) -> None:
    input()
    with open(os.path.join(path, name), "a") as file:
        if os.stat(os.path.join(path, name)).st_size > 0:
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(line + "\n")


def main() -> None:
    cmd_data = sys.argv
    d_index = cmd_data.index("-d") if "-d" in cmd_data else False
    f_index = cmd_data.index("-f") if "-f" in cmd_data else False
    path_to_file = "."

    if d_index:
        if f_index:
            path_part = cmd_data[d_index + 1:f_index]
        else:
            path_part = cmd_data[d_index + 1:]

        path_to_file = create_path(path_part)

    if f_index:
        file_name_part = cmd_data[f_index + 1]
        create_file(file_name_part, path_to_file)
