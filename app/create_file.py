import os
import argparse

from datetime import datetime


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", type=str, nargs="+", help="Create dir")
    parser.add_argument("-f", type=str, help="Create file")
    args = parser.parse_args()
    this_path = os.getcwd()
    if args.d is not None:
        this_path = create_directories(args.d)
    if args.f is not None:
        create_file(this_path, args.f)


def create_directories(new_way: list) -> str:
    this_path = os.path.join(*new_way)
    os.makedirs(this_path, exist_ok=True)
    return this_path


def create_file(this_path: str, filename: str) -> None:
    new_path = os.path.join(this_path, filename)
    with open(new_path, "a") as f:
        now = datetime.now()
        f.write(now.strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        some_content = input("Enter content line: ")
        while some_content != "stop":
            f.write(some_content + "\n")
            some_content = input("Enter content line: ")


if __name__ == "__main__":
    main()
