import argparse
import os
from argparse import Namespace
from datetime import datetime


def collect_data() -> list:
    lines = []
    line_counter = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            lines.append("\n")
            break
        lines.append(f"{line_counter} {line}\n")
        line_counter += 1
    return lines


def create_file(file_path: str) -> None:
    try:
        lines = collect_data()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, "a") as file:
            file.write(f"{timestamp}\n")
            file.writelines(lines)
    except OSError as e:
        print(f"Error: {e} while work with file")


def args_parser() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir", nargs="*", help="Directory path")
    parser.add_argument("-f", "--file", help="File path")
    return parser.parse_args()


def main() -> None:
    args = args_parser()

    directory_path = ""

    if args.dir:
        directory_path = os.path.join(*args.dir)
        os.makedirs(directory_path, exist_ok=True)
        print(f"{directory_path} directory created.")

    if args.file:
        file_path = os.path.join(directory_path, args.file)
        create_file(file_path)

    if not args.dir and not args.file:
        args.error("Neither '-d' or '-f' flag provided.")


if __name__ == "__main__":
    main()
