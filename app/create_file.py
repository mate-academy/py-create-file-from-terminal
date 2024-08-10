import os
import sys
from datetime import datetime
from typing import LiteralString


def create_directories(args: list[str]) -> LiteralString | str | bytes:
    dir_path = os.path.join(*args)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        counter = 1
        while True:
            text = input(f"Enter content line {counter} "
                         f"(or type stop to finish): ")
            if text.lower() == "stop":
                break
            file.write(f"{counter} {text}\n")
            counter += 1


def main() -> None:
    arg = sys.argv
    if "-d" in arg[:2]:
        d_index = arg.index("-d")
        if "-f" in arg:
            f_index = arg.index("-f")
            path_dir = arg[d_index + 1:f_index]
            full_dir_path = create_directories(path_dir)
            file_name = arg[f_index + 1]
            file_path = os.path.join(full_dir_path, file_name)
            create_file(file_path)
        else:
            path_dir = arg[d_index + 1:]
            create_directories(path_dir)
    elif "-f" in arg[:2]:
        f_index = arg.index("-f")
        file_name = arg[f_index + 1]
        if "-d" in arg:
            d_index = arg.index("-d")
            path_dir = arg[d_index + 1:]
            full_dir_path = create_directories(path_dir)
            file_path = os.path.join(full_dir_path, file_name)
        else:
            file_path = file_name
        create_file(file_path)


if __name__ == "__main__":
    main()
