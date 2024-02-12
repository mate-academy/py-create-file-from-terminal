import argparse
import os
from datetime import datetime


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)


def write_to_file(file_path: str, content: list) -> None:
    with open(file_path, "a") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for i, line in enumerate(content, start=1):
            file.write(f"{i} {line}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a file with content or directories."
    )
    parser.add_argument(
        "-d",
        "--directory",
        nargs="+",
        help="Directory path to create.",
        default=[]
    )
    parser.add_argument(
        "-f",
        "--file",
        help="File name to create with content."
    )
    args = parser.parse_args()

    directory_path = ""
    if args.directory:
        directory_path = os.path.join(*args.directory)
        create_directory(directory_path)

    if args.file:
        file_path = os.path.join(
            directory_path, args.file
        ) if directory_path else args.file
        write_to_file(file_path)


if __name__ == "__main__":
    main()
