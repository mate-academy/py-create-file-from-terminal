import argparse
import os
from datetime import datetime


def write_content_to_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                f.write("\n")
                break
            f.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    parser = argparse.ArgumentParser(description="Create file with content.")

    parser.add_argument(
        "-d", "--directory",
        type=str,
        nargs="+",
        help="Directory path where file should be created."
    )
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="File name to be created or appended.")

    args = parser.parse_args()

    dir_path = None

    if args.directory:
        dir_path = os.path.join(*args.directory)
        os.makedirs(dir_path, exist_ok=True)

    if args.file:
        file_name = args.file
        file_path = (
            os.path.join(dir_path, file_name)
            if dir_path
            else file_name
        )

        write_content_to_file(file_path)
