import os
import sys
from typing import TextIO


def fill_the_file(current_file: TextIO) -> None:
    import datetime
    current_file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    del datetime
    i = 0
    while True:
        i += 1
        current_input = input("Enter content line: ")
        if current_input == "stop":
            break
        current_file.write(f"\n{i} {current_input}")


def create_file(current_directory: str, file_name: str) -> None:
    os.makedirs(current_directory, exist_ok=True)
    if file_name:
        is_file_empty = True
        path = os.path.join(current_directory, file_name)
        if not os.path.exists(path):
            open(path, "x").close()
        else:
            with open(path, "r") as current_file:
                is_file_empty = current_file.read() == ""
        with open(path, "a") as current_file:
            if not is_file_empty:
                current_file.write("\n" * 2)
            fill_the_file(current_file)


def main() -> None:
    args = sys.argv[1:]
    dir_path = ""
    file_name = ""

    if "-f" in args:
        i = args.index("-f")
        file_name = args[i + 1]
        args.pop(i)
        args.pop(i)

    if "-d" in args:
        i = args.index("-d")
        dir_path = os.path.join(*args[i + 1:])

    create_file(dir_path, file_name)


if __name__ == "__main__":
    main()
