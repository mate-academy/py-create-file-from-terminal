import datetime
import sys
import os
from typing import TextIO


def get_dir() -> str:
    start_index = sys.argv.index("-d") + 1
    end_index = sys.argv.index("-f") if "-f" in sys.argv else len(sys.argv)
    path = sys.argv[start_index:end_index]
    return os.path.join(*path)


def get_file_name() -> str:
    return sys.argv[sys.argv.index("-f") + 1]


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def get_time() -> str:
    current_time = datetime.datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")


def write_user_lines(target_file: TextIO) -> None:
    target_file.write(f"{get_time()}\n")
    count = 1
    while True:
        text = input("Enter content line: ")
        if text.lower() == "stop":
            break
        target_file.write(f"{count} {text}\n")
        count += 1
    target_file.write("\n")


def create_file() -> None:
    dir_path = get_dir() if "-d" in sys.argv else None
    file_name = get_file_name() if "-f" in sys.argv else None

    if dir_path and file_name:
        create_dir(dir_path)
        file_path = os.path.join(dir_path, file_name)

    elif dir_path and not file_name:
        create_dir(dir_path)
        return

    elif not dir_path and file_name:
        file_path = file_name

    else:
        return

    with open(file_path, "a") as file:
        write_user_lines(file)


if __name__ == "__main__":
    create_file()
