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
        current_dir = os.path.join(*dir_names)
        os.makedirs(current_dir, exist_ok=True)


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"Enter content to append to '{file_path}' "
              f"(press Enter on an empty line to finish):")
        mode = "a"
    else:
        print(f"Enter content for {file_path} "
              f"(press Enter on an empty line to finish):")
        mode = "w"

    with open(file_path, mode) as file_object:
        block_number = 1
        while True:
            line = input(f"{block_number} Enter content line: ")
            if line == "stop":
                break
            now = datetime.datetime.now()
            file_object.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            file_object.write(f"{block_number} {line}\n")
            block_number += 1
            file_object.write("\n")


def main() -> None:
    dir_names = get_directory_names()
    create_directories(dir_names)
    file_name = ""
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
    file_path = (
        os.path.join(*dir_names, file_name)
        if dir_names or file_name else None
    )
    if file_path:
        create_file(file_path)


if __name__ == "__main__":
    main()
