import argparse
import os
from datetime import datetime


def write_file(filename: str | bytes) -> None:
    with open(filename, "a") as file:
        file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        count = 0
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            count += 1
            file.write(f"{count} {line}\n")
        file.write("\n")


def argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create file")
    parser.add_argument("-d", "--directory", help="Directory path", nargs="+")
    parser.add_argument("-f", "--file", help="File path")
    return parser.parse_args()


def create_dir() -> None:
    args = argument_parser()
    path = os.path.join("")
    if args.directory:
        path = os.path.join(*args.directory)
        os.makedirs(path, exist_ok=True)
    if args.file:
        path = os.path.join(path, args.file)
        write_file(path)


if __name__ == "__main__":
    create_dir()
