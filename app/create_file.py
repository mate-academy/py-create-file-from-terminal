import argparse
import os
from datetime import datetime


def create_directory(path_ending: list[str]) -> None:
    path = os.path.join(*path_ending)
    os.makedirs(path, exist_ok=True)


def create_file(filename: str, content_lines: list[str]) -> None:
    content = f'\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'

    for i, line in enumerate(content_lines, start=1):
        content += f"{i} {line}\n"

    with open(filename, "a") as file:
        file.write(content)


def main() -> None:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", nargs="+")
    group.add_argument("-f")

    args = parser.parse_args()

    if args.d:
        create_directory(args.d)

    if args.f:
        filepath = os.path.join(*args.d, args.f) if args.d else args.f
        content_lines = []
        while True:
            line = input("Enter content line or type 'stop' to end: ")
            if line == "stop":
                break
            content_lines.append(line)
        create_file(filepath, content_lines)


if __name__ == "__main__":
    main()
