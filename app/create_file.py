from sys import argv
import os
from datetime import datetime


def create_file_dirs() -> None:

    parent_dir = "app"

    if "-d" in argv:
        parent_dir = create_dirs(argv, parent_dir)

    if "-f" in argv:
        create_file(argv, parent_dir)


def create_dirs(arg: list, parent_dir: str) -> str:

    index_d = arg.index("-d")
    last_index_d = arg.index("-f") if "-f" in arg[index_d:] else len(arg)

    for directory in arg[index_d + 1:last_index_d]:
        parent_dir = os.path.join(parent_dir, directory)
        os.makedirs(parent_dir, exist_ok=True)

    return parent_dir


def create_file(arg: list, parent_dir: str) -> None:

    page_number = 1
    file_index = arg.index("-f")
    file_name = os.path.join(parent_dir, arg[file_index + 1])

    with open(file_name, "a") as source_file:
        if not os.stat(file_name).st_size == 0:
            source_file.write("\n\n")
        source_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        current_line = input("Enter content line:")
        while not current_line == "stop":
            source_file.write(f"\n{page_number} {current_line}")
            page_number += 1
            current_line = input("Enter content line:")


if __name__ == "__main__":
    create_file_dirs()
