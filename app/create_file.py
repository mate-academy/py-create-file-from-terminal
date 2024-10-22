import os
import argparse
from datetime import datetime


def create_directory(path_list: list) -> str:
    path = os.path.join(*path_list)
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory '{path}' created.")
    else:
        print(f"Directory '{path}' already exists.")
    return path


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Appending new content.")
    else:
        print(f"File '{file_path}' created.")

    with open(file_path, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and files with content"
    )
    parser.add_argument(
        "-d", "--directory", nargs="+", help="Directory path to create"
    )
    parser.add_argument(
        "-f", "--file", help="File name to create or append content"
    )

    args = parser.parse_args()

    if args.directory:
        dir_path = create_directory(args.directory)
    else:
        dir_path = os.getcwd()

    if args.file:
        file_path = os.path.join(dir_path, args.file)
        create_file(file_path)


if __name__ == "__main__":
    main()
