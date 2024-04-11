import os
import argparse
from datetime import datetime


def create_file(directory: str, filename: str, content_lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(filename, str):
        raise TypeError
    filepath = os.path.join(directory, filename)

    mode = "a" if os.path.exists(filepath) else "w"
    with open(filepath, mode) as file:
        if mode == "w":
            file.write(timestamp + "\n")
        file.writelines(content_lines)


def get_content_lines() -> list:
    content_lines = []
    idx = 1
    while True:
        line = input(f"Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines += f"{idx} {line}\n"
        idx += 1
    return content_lines


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directory or file with content"
    )
    parser.add_argument("-d", "--directory", nargs="+", help="Directory path")
    parser.add_argument("-f", "--file", help="File name")

    args = parser.parse_args()

    if args.directory:
        directory_path = os.path.join(*args.directory)
        os.makedirs(directory_path, exist_ok=True)
        if args.file:
            content_lines = get_content_lines()
            create_file(directory_path, args.file, content_lines)
    elif args.file:
        content_lines = get_content_lines()
        create_file(".", args.file, content_lines)


if __name__ == "__main__":
    main()
