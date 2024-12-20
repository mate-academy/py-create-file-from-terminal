import os
import sys
from datetime import datetime


def create_content_for_file() -> list[str]:
    lines = [f"{datetime.now()}\n"]
    number_of_line = 1
    line = input("Enter content line:")
    lines.append(f"{number_of_line} {line}\n")
    while line != "stop":
        line = input("Enter content line:")
        number_of_line += 1
        lines.append(f"{number_of_line} {line}\n")
    lines.append("\n")
    return lines


def create_dirs(path: str, terminal_args: list[str]) -> str:
    index = terminal_args.index("-f")
    path_dir = os.path.join("/".join(sys.argv[2:index]))
    os.makedirs(path_dir)
    dir_path = os.path.join(path, path_dir)
    return dir_path


def write_file_content(path: str, file_name: str, content: str) -> None:
    with open(os.path.join(path, file_name), "a+") as file:
        file.writelines(content)


def create_file(terminal_args: list[str]) -> None:
    path = os.getcwd()
    file_name = terminal_args[-1]
    if "-d" in terminal_args:
        path = create_dirs(path, terminal_args)
    content = create_content_for_file()
    write_file_content(path, file_name, content)


if __name__ == "__main__":
    create_file(sys.argv)
