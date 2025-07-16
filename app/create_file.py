import os
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(
    prog="File-Creator",
    description="Created full path from command line "
                "with file if needed, append new lines "
                "if file exists")
parser.add_argument("-d", "--dir", nargs="*", help="Directory path")
parser.add_argument("-f", "--file", help="File name")
args = parser.parse_args()


def create_file(filedir: str) -> None:
    result_data = []
    new_line = ""

    while new_line != "stop":
        if new_line:
            result_data.append(new_line)
        new_line = input("Enter content line: ")

    file_exist = os.path.exists(filedir)

    with open(filedir, "a") as file:
        page_number = 1

        if file_exist:
            file.write("\n")

        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for elem in result_data:
            file.write(f"{page_number} {elem}\n")
            page_number += 1


def main() -> None:
    if args.dir:
        path_dir = os.path.join(*args.dir)
        os.makedirs(path_dir, exist_ok=True)

    if args.file:
        if args.dir:
            file_path = os.path.join(*args.dir, args.file)
        else:
            file_path = args.file
        create_file(file_path)

    if not args.dir and not args.file:
        print("You need to specify a directory or file name")


if __name__ == "__main__":
    main()
