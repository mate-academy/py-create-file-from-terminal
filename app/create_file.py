import argparse
import os

from datetime import datetime


TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_args_from_command() -> tuple:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d",
        dest="dirs",
        type=str,
        nargs="*",
        help="List of dirs"
    )
    parser.add_argument(
        "-f",
        dest="file_name",
        type=str,
        nargs=1,
        help="file name"
    )
    args = parser.parse_args()

    return args.dirs, args.file_name


def build_and_get_path(dirs: list[str], file_name: list[str]) -> str:
    path = ""

    if dirs:
        path = os.path.join(*dirs)
        try:
            os.makedirs(path)
        except FileExistsError:
            print("Folders already exists")

    if file_name:
        return os.path.join(path, *file_name)

    return ""


def file_cli(path: str):
    with open(path, "a") as file:
        timestamp = datetime.now().strftime(TIME_FORMAT)
        file.write(f"{timestamp}\n")

        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{line_num} {line}\n")
            line_num += 1


def main():
    args = get_args_from_command()

    path = build_and_get_path(*args)

    if path:
        file_cli(path)


main()
