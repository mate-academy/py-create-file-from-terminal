import argparse
import os
from datetime import datetime
from typing import Any


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def get_file_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def create_file_from_args(args: Any) -> None:
    if args.route:
        dir_path = os.path.join(*args.route)

        create_directory(dir_path)
        file_path = os.path.join(dir_path, args.file)
    else:
        file_path = args.file

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = "\n".join([
        timestamp, *[f"{i+1} {line}" for i, line in enumerate(input_lines)]
    ])
    with open(file_path, "a") as f:
        f.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--route", nargs="*", help="directory path")
    parser.add_argument("-f", "--file", help="file name")
    args = parser.parse_args()

    if args.route is None and args.file is None:
        parser.error("Either -d or -f must be provided")
    elif args.file:
        input_lines = get_file_content()
        create_file_from_args(args)
    else:
        create_directory(os.path.join(*args.route))
