import os
from datetime import datetime
from typing import List
import argparse


def create_path(directories: List[str]) -> str:
    path = os.path.join(*directories)
    return path


def create_file(
        directory: str,
        file_name: str,
        content_lines: List[str]
) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path = os.path.join(directory, file_name)

    with open(file_path, "w") as file:
        file.write(timestamp + "\n")
        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")


def get_content_lines() -> List[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directories", nargs="+", required=False)
    parser.add_argument("-f", "--file_name", required=False)

    args = parser.parse_args()

    if args.directories:
        directory_path = create_path(args.directories)
        os.makedirs(directory_path, exist_ok=True)

        if args.file_name:
            create_file(directory_path, args.file_name, get_content_lines())
    elif args.file_name:
        create_file(os.getcwd(), args.file_name, get_content_lines())


if __name__ == "__main__":
    main()
