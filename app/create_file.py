import sys
import os
from datetime import datetime
from typing import TextIO


def parse_arguments() -> tuple[str, list]:
    arguments = sys.argv
    file_to_create = None
    directories = []

    if "-f" in arguments and (arguments.index("-f") + 1) < len(arguments):
        file_to_create = arguments[arguments.index("-f") + 1]

    if "-d" in arguments:
        directories.extend(
            directory
            for directory
            in arguments[arguments.index("-d") + 1:]
            if directory != "-f"
        )

    return file_to_create, directories


def create_directories(directories: list[str]) -> str:
    if directories:
        result_dir = os.path.join(os.getcwd(), *directories)
        os.makedirs(result_dir, exist_ok=True)
        return result_dir
    return ""


def create_file(file_to_create: str, result_dir: str) -> None:
    if file_to_create:
        file_path = os.path.join(os.getcwd(), result_dir, file_to_create)
        with open(file_path, "w") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            write_content(f)


def write_content(file_to_change: TextIO) -> None:
    line_counter = 0
    while True:
        line_counter += 1
        answer = input("Enter content line: ")

        if answer == "stop":
            file_to_change.write("\n")
            break

        file_to_change.write(f"\n{line_counter} {answer}")


def main() -> None:
    file_to_create, directories = parse_arguments()
    result_dir = create_directories(directories)
    create_file(file_to_create, result_dir)


if __name__ == "__main__":
    main()
