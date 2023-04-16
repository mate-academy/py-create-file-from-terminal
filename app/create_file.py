import os
import sys
import datetime
from typing import List


def get_directory_names() -> List[str]:
    dir_names = []
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f") if "-f" in sys.argv else None
        dir_names = (
            sys.argv[d_index + 1:]
            if f_index is None or d_index > f_index else
            sys.argv[d_index + 1: f_index]
        )
    return dir_names


def create_directories(dir_names: List[str]) -> None:
    if dir_names:
        directory_path = os.path.join(*dir_names)
        os.makedirs(directory_path, exist_ok=True)


def create_file(file_path: str) -> None:
    now = datetime.datetime.now()
    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file_object:
        if mode == "w":
            file_object.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        else:
            file_object.write(f"\n{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        block_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            if line.strip():
                file_object.write(f"{block_number} {line}\n")
                block_number += 1


def main() -> None:
    dir_names = get_directory_names()
    create_directories(dir_names)
    file_name = ""
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
    file_path = (
        os.path.join(*dir_names, file_name)
        if dir_names and file_name else file_name
    )
    if file_path:
        create_file(file_path)


if __name__ == "__main__":
    main()
