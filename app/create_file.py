import os
import argparse

from datetime import datetime


def parse_args() -> argparse.Namespace:
    parses = argparse.ArgumentParser()
    parses.add_argument("-d", "--directory",
                        type=str, nargs="+", help="create directory")
    parses.add_argument("-f", "--file", type=str, help="create file")
    return parses.parse_args()


def create_directory(directory: list[str]) -> None:
    os.makedirs(os.path.join(*directory), exist_ok=True)


def create_file(directory: list[str] | None, file_name: str) -> None:
    if directory is None:
        directory = ["."]
    with open(os.path.join(*directory, file_name), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n\n")
                break
            file.write(f"\n{line_number} {content}")
            line_number += 1


if __name__ == "__main__":
    args = parse_args()
    if args.directory:
        create_directory(args.directory)
    if args.file:
        create_file(args.directory, args.file)
