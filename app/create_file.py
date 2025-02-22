import sys
import os
from datetime import datetime
from typing import Any


def create_dir(dir_path: Any) -> None:
    os.makedirs(dir_path, exist_ok=True)


def create_file(path_to_file: Any) -> None:
    with open(path_to_file, "a") as file_in:
        date_now = datetime.now()
        line = date_now.strftime("%Y-%m-%d %H:%M:%S")
        while True:
            if line.lower() == "stop":
                break
            file_in.write(line + "\n")
            line = str(input("Enter content line: "))


def create_path() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d")
        file_index = sys.argv.index("-f")
        directory_path = os.path.join(*sys.argv[dir_index + 1:])
        file_path = os.path.join(*sys.argv[file_index + 1:])
        if dir_index < file_index:
            directory_path = os.path.join(*sys.argv[dir_index + 1:file_index])
        else:
            file_path = os.path.join(*sys.argv[file_index + 1:dir_index])
        create_dir(directory_path)
        create_file(os.path.join(directory_path, file_path))

    elif "-d" in sys.argv:
        create_dir(os.path.join(*sys.argv[2:]))

    elif "-f" in sys.argv:
        create_file(os.path.join(*sys.argv[2:]))


if __name__ == "__main__":
    create_path()
