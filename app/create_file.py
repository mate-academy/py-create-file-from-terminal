import os
import sys
from datetime import datetime


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    """Split terminal arguments into directories and file name."""
    directories = []
    file_name = None
    current_flag = None

    for argument in arguments:
        if argument in ("-d", "-f"):
            current_flag = argument
        elif current_flag == "-d":
            directories.append(argument)
        elif current_flag == "-f":
            file_name = argument

    return directories, file_name


def create_directory(directories: list[str]) -> str:
    """Create nested directories and return the path to them."""
    directory_path = os.path.join("", *directories)
    os.makedirs(directory_path, exist_ok=True)

    return directory_path


def create_file(file_path: str) -> None:
    """Create (or append to) the file and fill it with numbered lines."""
    with open(file_path, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_number = 1

        while True:
            line = input("Enter content line: ")

            if line == "stop":
                break

            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])
    directory_path = ""

    if directories:
        directory_path = create_directory(directories)

    if file_name:
        create_file(os.path.join(directory_path, file_name))


if __name__ == "__main__":
    main()
