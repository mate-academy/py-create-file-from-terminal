import os
import argparse
from datetime import datetime


def create_file(directory: str, filename: str, content_lines: list) -> None:

    filepath = os.path.join(directory, filename)

    try:
        with open(filepath, "a") as file:
            file.writelines(content_lines)
    except OSError:
        raise


def get_content_lines() -> list:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = [timestamp + "\n"]
    idx = 1
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(f"{idx} {line}\n")
        idx += 1
    content_lines.append("\n")
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
    elif args.file:
        content_lines = get_content_lines()
        create_file(".", args.file, content_lines)


if __name__ == "__main__":
    main()
