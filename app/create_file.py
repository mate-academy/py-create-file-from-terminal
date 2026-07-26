import sys
import os
from datetime import datetime as dt


def create_file(file_name: str, full_path: str) -> None:
    file_name = os.path.join(full_path, file_name)
    lines = [dt.strftime(dt.now(), "%Y-%m-%d %H:%M:%S") + "\n", ]
    count_line = 0
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            lines.append("\n")
            break
        count_line += 1
        lines.append(f"{count_line} {line}\n")

    with open(file_name, "a") as file:
        file.writelines(lines)


def create_dir(dir_ls: list) -> str:
    full_path = os.path.join(*dir_ls)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
    return full_path


def create_dir_file() -> None:
    full_path = os.getcwd()
    dir_ls = [full_path]
    args = sys.argv
    if "-d" in args and "-f" in args:
        dir_ls.extend(args[2: args.index("-f")])
        full_path = create_dir(dir_ls)
        create_file(args[-1], full_path)
    elif "-d" in args:
        dir_ls.extend(args[2:])
        create_dir(dir_ls)
    elif "-f" in args:
        create_file(args[-1], full_path)


if __name__ == "__main__":
    create_dir_file()
