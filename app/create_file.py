import os
from datetime import datetime
from pathlib import Path
"""
create_file("python create_file.py -d dir1 dir2")
create_file("python create_file.py -f file.txt")
create_file("python create_file.py -d dir1 dir2 -f file.txt")
create_file("python create_file.py -f file.txt -d dir1 dir2")
"""


def parse_command(input_string: str) -> tuple[list, str] | None:
    _, _, flag, *path_ = input_string.split()
    if flag == "-d":
        if "-f" in path_:
            return path_[0:-2], path_[-1]
        return path_[0:], ""
    elif flag == "-f":
        if "-d" in path_:
            return path_[2:], path_[0]
        return [], path_[-1]


def create_file(command: str) -> None:
    dr, filename = parse_command(command)
    if not dr:
        write_content(filename)
    elif not filename:
        dir_path = os.path.join(*dr)
        os.makedirs(dir_path, exist_ok=True)
    elif dr and filename:
        pat = dr + [filename]
        dir_path = os.path.join(*pat)
        Path(dir_path).parent.mkdir(exist_ok=True, parents=True)
        write_content(dir_path)


def write_content(file_path: str) -> None:
    with open(file_path, "a") as target_file:
        current_time = f"{datetime.now():%Y-%m-%d %H:%M:%S}"
        target_file.write(current_time + "\n")
        number = 0
        while True:
            new_line = input("Enter content line:")
            if new_line == "stop":
                target_file.write("\n")
                break
            number += 1
            target_file.write(f"{number} {new_line} \n")
