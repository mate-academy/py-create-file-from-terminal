import datetime
import os
import sys
from typing import Any


def parse_arguments(args: list[str]) -> Any:
    dir_path = "."
    file_name = None

    if "-d" in args:
        dir_index = args.index("-d") + 1
        directories = []

        for i in range(dir_index, len(args)):
            if args[i].startswith("-"):
                break
            directories.append(args[i])

        if directories:
            dir_path = os.path.join(*directories)

    if "-f" in args:
        file_index = args.index("-f") + 1
        if file_index >= len(args) or args[file_index].startswith("-"):
            print("Error: No file name provided after -f")
            sys.exit(1)
        file_name = args[file_index]

    return dir_path, file_name


def create_directory(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)


def write_to_file(file_name: str) -> None:
    date_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Перевіряємо, чи файл вже існує і чи він непорожній
    file_exists = os.path.exists(file_name)
    is_empty = not file_exists or os.path.getsize(file_name) == 0

    with open(file_name, "a") as file:
        if not is_empty:
            file.write("\n")

        file.write(f"{date_today}\n")
        counter = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(f"{counter} {text}\n")
            counter += 1


if __name__ == "__main__":
    args = sys.argv[1:]
    dir_path, file_name = parse_arguments(args)

    if dir_path != ".":
        create_directory(dir_path)

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        write_to_file(file_path)
