import os
from datetime import datetime
import argparse


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1
    print(f"File '{file_path}' created/updated successfully.")


def parse_arguments() -> None:
    parser = argparse.ArgumentParser(
        description="Create or update a file in specified directory."
    )
    parser.add_argument(
        "-d",
        "--directories",
        nargs="*",
        help="Directories where the file should be created"
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Name of the file to create or update"
    )

    args = parser.parse_args()

    if not args.directories and not args.file:
        parser.print_usage()
        return

    if args.directories:
        path = os.path.join(*args.directories)
        os.makedirs(path, exist_ok=True)
    else:
        path = ""

    if args.file:
        file_path = os.path.join(str(path), args.file) if path else args.file
        create_file(file_path)
    else:
        print("File name not provided.")


if __name__ == "__main__":
    parse_arguments()
