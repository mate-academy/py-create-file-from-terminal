import argparse
import os
from datetime import datetime


class MissingArgumentError(Exception):
    def __str__(self) -> str:
        return ("You`ve missed some arguments! "
                "Use -h to see the usage of program")


def create_dirs(directories: list) -> str:
    dirs = os.path.join(*directories)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    return dirs


def write_file(path_to_file: str) -> None:
    with open(path_to_file, "a") as output_file:
        date = datetime.now().strftime("%y-%m-%d %H:%M:%S")
        output_file.write(f"{date}\n")
        page_number = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            output_file.write(f"{page_number} {text}\n")
            page_number += 1
        output_file.write("\n")


def create_files() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+", help="used to create directories")
    parser.add_argument("-f", type=str, help="used to create file")
    args = parser.parse_args()
    if args.d and args.f:
        dirs = create_dirs(args.d)
        path_to_file = os.path.join(dirs, args.f)
        write_file(path_to_file)

    elif args.d:
        create_dirs(args.d)
    elif args.f:
        write_file(args.f)
    else:
        raise MissingArgumentError


if __name__ == "__main__":
    create_files()
