import os
import sys
from datetime import datetime
from typing import LiteralString


def create_dirs(sys_data: list, f_index: int) -> LiteralString | str | bytes:
    d_index = sys_data.index("-d")
    if f_index > d_index:
        d_data = sys_data[d_index + 1: f_index]
    else:
        d_data = sys_data[d_index + 1:]
    os.makedirs(os.path.join(*d_data), exist_ok=True)
    return os.path.join(*d_data, sys_data[f_index + 1])


def write_data(path: LiteralString | str | bytes) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    counter = 1
    info_from_user = f"{current_time}\n"

    while True:
        line_from_user = input("Enter content line: ")
        if line_from_user == "stop":
            info_from_user += "\n"
            break
        info_from_user += f"{counter} {line_from_user}\n"
        counter += 1

    with open(path, "a") as file:
        file.write(info_from_user)


def create_file() -> None:
    sys_data = sys.argv[1:]
    f_index = sys_data.index("-f")
    if "-d" in sys_data:
        path = create_dirs(sys_data, f_index)
    else:
        path = os.path.join(sys_data[f_index + 1])
    write_data(path)


if __name__ == "__main__":
    create_file()
