import argparse
import os
from datetime import datetime


def create_directory(path_parts: list) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_file(file_path: str) -> None:
    content = []

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content.append(f"{timestamp}")

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    numbered_content = [
        f"{i} {line}" for i, line in enumerate(content[1:], start=1)
    ]

    with open(file_path, "a") as file:
        file.write("\n".join([content[0]] + numbered_content) + "\n")

    print(f"Content written to: {file_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directories and files with content."
    )

    parser.add_argument(
        "-d", "--directories", nargs="*", help="Directory path to create."
    )

    parser.add_argument(
        "-f", "--file", help="File name to create and write content to."
    )

    args = parser.parse_args()

    if args.directories:
        create_directory(args.directories)

    if args.file:
        file_name = args.file
        if args.directories:
            file_name = os.path.join(*args.directories, args.file)
        create_file(file_name)


if __name__ == "__main__":
    main()
