import argparse
import os
import sys
from datetime import datetime
from typing import Optional


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+", type=str)
    parser.add_argument("-f", type=str)
    args = parser.parse_args(sys.argv[1:])

    if not args.d and not args.f:
        raise ValueError("At leas one flag should be specified: -d or -f")

    return args


def create_directory(path: Optional[str]) -> None:
    if path:
        os.makedirs(path, exist_ok=True)


def build_file_path(
    dirs: Optional[list[str]],
    filename: Optional[str]
) -> str | None:
    if dirs and filename:
        return os.path.join(os.path.join(*dirs), filename)
    elif filename:
        return filename
    return None


def write_to_file(file_path: str) -> None:
    contents_str_list = []

    if os.path.exists(file_path) and os.stat(file_path).st_size != 0:
        contents_str_list.append("\n")

    contents_str_list.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
    line_number = 0
    while True:
        new_line = input("Enter content line: ")
        if new_line == "stop":
            break
        line_number += 1
        contents_str_list.append(f"{line_number} {new_line}\n")

    try:
        with open(file_path, "a") as file:
            file.write("".join(contents_str_list))
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def create_file() -> None:
    args = parse_args()
    path = str(os.path.join(*args.d)) if args.d else None
    create_directory(path)
    file_path = build_file_path(args.d, args.f)
    if file_path:
        write_to_file(file_path)


if __name__ == "__main__":
    create_file()
