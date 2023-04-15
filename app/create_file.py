import os
import sys
import datetime
from typing import List


def get_directory_names() -> list:
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


def get_file_name() -> str:
    file_name = ""
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
    return file_name


def create_directories(dir_names: List[str]) -> None:
    if dir_names:
        directory_path = os.path.join(*dir_names)
        os.makedirs(directory_path, exist_ok=True)


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists.")
        print(f"Enter content to append to '{file_path}' "
              f"(press Enter on an empty line to finish):")
        content = ""
        while True:
            line = input()
            if line == "stop":
                break
            content += line + "\n"
        with open(file_path, "a") as f:
            f.write(content)
    else:
        with open(file_path, "w") as f:
            # Adding date and time to the file
            now = datetime.datetime.now()
            f.write(f"Creation time: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
            print(f"Enter content for {file_path} "
                  f"(press Enter on an empty line to finish):")
            content = ""
            while True:
                line = input()
                if line == "stop":
                    break
                content += line + "\n"
            f.write(content)
            f.write("\n")


def main() -> None:
    dir_names = get_directory_names()
    file_name = get_file_name()
    create_directories(dir_names)
    file_path = (
        os.path.join(*dir_names, file_name)
        if dir_names or file_name else None
    )
    if file_path:
        create_file(file_path)


if __name__ == "__main__":
    main()
