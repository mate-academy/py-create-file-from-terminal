import os
import argparse
from datetime import datetime


def create_directory(path: any) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_path: any) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+", help="path")
    parser.add_argument("-f", "--file", help="file name")

    args = parser.parse_args()

    if args.directory and args.file:
        directory_path = os.path.join(*args.directory)
        create_directory(directory_path)
        file_path = os.path.join(*args.directory, args.file)
        create_file(file_path)
    elif args.directory:
        directory_path = os.path.join(*args.directory)
        create_directory(directory_path)
    elif args.file:
        create_file(args.file)
