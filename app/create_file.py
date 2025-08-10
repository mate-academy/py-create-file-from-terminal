import argparse
import os
from datetime import datetime


def create_path(*args) -> str:
    path = os.path.join(*args)
    return path


def create_directory(directories: list) -> None:
    directory_path = create_path(*directories)
    os.makedirs(directory_path, exist_ok=True)


def write_to_file(file_name: str) -> None:
    with open(f"{file_name}", "a+") as created_file:
        first_line_ever = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        created_file.write(first_line_ever + "\n")
        counter_lines = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            counter_lines += 1
            content = f"{counter_lines} {line}"
            created_file.write(content + "\n")
        created_file.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="script to create files and directories"
    )

    parser.add_argument(
        "-d",
        nargs="+",
        metavar="directory",
        help="'create directory' flag"
    )
    parser.add_argument(
        "-f",
        nargs="+",
        metavar="filename",
        help="'create file' flag"
    )

    options = parser.parse_args()

    if options.d and options.f:
        create_directory(options.d)
        write_to_file(create_path(*options.d, *options.f))
    elif options.f:
        write_to_file(*options.f)
    elif options.d:
        create_directory(options.d)
