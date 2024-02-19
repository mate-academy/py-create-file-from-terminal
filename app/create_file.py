from datetime import datetime
import os.path
import sys
import argparse


def create_parse() -> argparse:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--filepath", nargs="+", default=None)
    parser.add_argument("-f", "--filename", nargs="+", default=None)
    return parser


def create_folders(folders_path: list) -> str | bytes:
    if folders_path:
        path = os.path.join(*folders_path)
        os.makedirs(path, exist_ok=True)
        return path
    return ""


def file_handler(file_path: str) -> None:
    with open(file_path, "a") as file:
        lines = []
        line_number = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            lines.append(f"{line_number} {text}\n")
            line_number += 1
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_datetime}\n{''.join(lines)}\n")


if __name__ == "__main__":
    parser_args = create_parse()
    args = parser_args.parse_args(sys.argv[1:])
    folders = create_folders(folders_path=args.filepath)
    if args.filename:
        filepath = os.path.join(f"{folders}", *args.filename)
        file_handler(filepath)
