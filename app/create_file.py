import os
from datetime import datetime
from typing import Any
import argparse


def create_directory(dirs: Any) -> None:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created or already exists: {path}")


def create_file(file_path: Any) -> None:

    print("Enter content lines (type 'stop' on a new line to finish):")
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            lines.append("")
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(f"{timestamp}\n")

        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")

    print(f"File created/updated: {file_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and files with content."
    )
    parser.add_argument(
        "-d",
        "--dirs",
        nargs="+",
        help="Directories to create"
    )
    parser.add_argument(
        "-f",
        "--file",
        help="File to create or append content to"
    )

    args = parser.parse_args()

    if args.dirs:
        create_directory(args.dirs)

    if args.file:
        file_path = os.path.join(*args.dirs, args.file) \
            if args.dirs else args.file
        create_file(file_path)


if __name__ == "__main__":
    main()
