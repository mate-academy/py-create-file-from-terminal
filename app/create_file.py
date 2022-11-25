import sys
import os
from datetime import datetime as dt


def create_file(file_ls: list, full_path: str) -> None:
    for file_name in file_ls:
        with open(os.path.join(full_path, file_name), "a") as file:
            file.write(dt.strftime(dt.now(), "%Y-%m-%d %H:%M:%S") + "\n")
            count_line = 0
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    file.write("\n")
                    break
                count_line += 1
                file.write(f"{count_line} {line}\n")


def create_dir_file() -> None:
    mode = None
    file_ls = []
    full_path = os.getcwd()
    for arg in sys.argv:
        if arg == "-d":
            mode = "create_dir"
            continue
        if arg == "-f":
            mode = "create_file"
            continue

        if mode == "create_dir":
            full_path = os.path.join(full_path, arg)
        elif mode == "create_file":
            file_ls.append(arg)

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    create_file(file_ls, full_path)


if __name__ == "__main__":
    create_dir_file()
