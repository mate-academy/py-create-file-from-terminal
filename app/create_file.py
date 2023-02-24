import argparse
import os
import datetime


def file_content(name_file: str) -> None:
    content = []
    command = input("Enter content line: ")
    while command != "stop":
        content.append(command)
        command = input("Enter content line: ")
    with open(f"{name_file}.txt", "a") as file:
        now = datetime.datetime.now()
        file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        page_number = 1
        for line in content:
            file.write(f"{page_number}.{line}\n")
            page_number += 1


def make_directory() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    if args.directory:
        direct_path = os.path.join(*args.directory)
        os.makedirs(direct_path)
        if args.file:
            file_path = os.path.join(direct_path, args.file)
            os.makedirs(file_path)
            file_content(file_path)
    elif args.file:
        file_content(args.file)
