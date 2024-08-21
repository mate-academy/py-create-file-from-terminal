import os
import sys
import time
from datetime import datetime


def create_path(path_dir: str) -> None:
    try:
        os.makedirs(path_dir, exist_ok=True)
    except OSError as e:
        print(f"Failed to create directory '{path_dir}': {e}")


def create_content(file_path: str) -> None:
    style = "a" if os.path.exists(file_path) else "w"
    with open(file_path, style) as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    line_number = 1

    while True:
        line_content = input(f"Enter content line {line_number}: ")
        if line_content.lower() == "stop":
            break
        file.write(f"{line_number} {line_content}\n")
        line_number += 1


def main():
    args = sys.argv[1:]
    if "-d" in args:
        dir_index = args.index("-d") + 1
        dir_path = os.path.join(*args[dir_index:])
    else:
        dir_path = None

    if "-f" in args:
        file_index = args.index("-f") + 1
        file_name = args[file_index]
    else:
        file_name = None

    if dir_path:
        create_path(dir_path)

    if file_name:
        if dir_path:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name

        create_content(file_path)
    elif dir_path:
        create_path(dir_path)


if __name__ == "__main__":
    main()