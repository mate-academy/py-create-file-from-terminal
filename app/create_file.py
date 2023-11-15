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

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n" * 2)

        file.write(timestamp + "\n")
        file.write("\n".join(content_lines))


def get_content_lines() -> List[str]:
    content_lines = []
    counter = 0

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        counter += 1
        content_lines.append(f"{counter} {line}")
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
