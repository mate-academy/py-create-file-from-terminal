import argparse
import datetime
import os
import sys

command_line_args = sys.argv
parser = argparse.ArgumentParser()


def parser_dirs() -> None:
    parser.add_argument(
        "-d", "--dirs",
        nargs="+",
        required=False,
        help="Список директорій (dir1 dir2 ...)"
    )


def parser_file() -> None:
    parser.add_argument(
        "-f", "--file",
        required=False,
        help="Назва файлу"
    )


def creating_file(full_file_path: str) -> None:
    with open(full_file_path, "a") as file:
        if (os.path.exists(full_file_path)
                and os.path.getsize(full_file_path) != 0):
            file.write("\n")
        file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        count_line = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{count_line} {line}\n")
            count_line += 1


parser_dirs()
parser_file()
args = parser.parse_args()
base_path = os.getcwd()
if args.dirs:
    base_path = os.path.join(base_path, *args.dirs)
    os.makedirs(base_path, exist_ok=True)

if args.file:
    file_path = os.path.join(base_path, args.file)
    creating_file(file_path)
    print(f"File created/updated: {file_path}")
