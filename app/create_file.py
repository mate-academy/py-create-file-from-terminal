import argparse
import os
from datetime import datetime


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory",
                        type=str, nargs="*", help="creates directory")
    parser.add_argument("-f", "--file", type=str, help="creates a file")
    return parser.parse_args()


def process_directory(directory: list[str]) -> None:
    os.makedirs(os.path.join(*directory), exist_ok=True)


def process_file(directory: list[str], filename: str) -> None:
    with open(os.path.join(*directory or "", filename), "a") as file:
        file.write(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
        line_number = 1
        while True:
            data = input("Enter content line: ")
            if data == "stop":
                file.write("\n\n")
                break
            file.write(f"\n{line_number} {data}")
            line_number += 1


if __name__ == "__main__":
    args = parse_args()
    if args.directory:
        process_directory(args.directory)
    if args.file:
        process_file(args.directory, args.file)
