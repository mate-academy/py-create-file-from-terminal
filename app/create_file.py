import os
import argparse

from datetime import datetime


def create_directory(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)


def create_file(file_creation: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_content = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        file_content.append(line)

    with open(file_creation, "a") as new_file:
        new_file.write(timestamp)
        for i, line in enumerate(file_content, start=1):
            new_file.write(f"{i} {line}\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+", help="directory path")
    parser.add_argument("-f", help="file name")
    args = parser.parse_args()

    if args.d:
        directory_path = os.path.join(*args.d)
        create_directory(directory_path)

    if args.f:
        create_file(args.f)


if __name__ == "__main__":
    main()
