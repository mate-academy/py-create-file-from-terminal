import argparse
import datetime
import os
import sys


def create_directory(directory: str) -> None:
    path = os.path.join(os.getcwd(), directory)
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        current_date = datetime.datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        for line in sys.stdin:
            if line.rstrip() == "stop":
                break
            file.write(str(line_number) + " " + line)
            line_number += 1
        file.write("\n")


def main_function() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file")
    args = parser.parse_args()
    if args.directory and args.file:
        create_directory(os.path.join(*args.directory))
        create_file(os.path.join(os.path.join(*args.directory), args.file))
    elif args.directory:
        create_directory(os.path.join(*args.directory))
    elif args.file:
        create_file(args.file)


main_function()
