from datetime import datetime

from sys import argv

from os import makedirs
from os.path import join, exists


def create_directory(path_parts: list[str]) -> None:
    path = join(*path_parts)
    if not exists(path):
        makedirs(path)


def create_file(file_name: str) -> None:
    if exists(file_name):
        mode = "a"
    else:
        mode = "w"

    with open(file_name, mode) as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")

        line_number = 1
        content = input("Enter content line: ")
        while content != "stop":
            f.write(f"{line_number} {content}\n")
            line_number += 1
            content = input("Enter content line: ")


def main() -> None:
    args = argv[1:]

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")
        path_parts = args[d_index + 1:f_index]
        file_name = join(*path_parts, args[f_index + 1])
        create_directory(path_parts)
        create_file(file_name)

    elif "-d" in args:
        d_index = args.index("-d")
        path_parts = args[d_index + 1:]
        create_directory(path_parts)

    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        create_file(file_name)


if __name__ == "__main__":
    main()
