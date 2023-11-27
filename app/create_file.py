import os
import argparse
from typing import List
import datetime


def create_directories(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def append_content_to_file(
        filepath: str,
        content_lines: List[str],
        timestamp: str
) -> None:
    with open(filepath, "a", encoding="utf-8") as file:
        if os.path.getsize(filepath) == 0:
            file.write(timestamp)
        else:
            file.write("\n" + timestamp)
        for index, line in enumerate(content_lines, start=1):
            file.write(f"{index} {line}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a file with content.")
    parser.add_argument("-d",
                        "--directory",
                        nargs="+",
                        help="Directory path to create")
    parser.add_argument("-f", "--filename", help="File name to create")
    args = parser.parse_args()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
    directory_path = ""
    if args.directory:
        directory_path = os.path.join(*args.directory)
        create_directories(directory_path)

    if args.filename:
        filepath = (os.path.join(directory_path, args.filename)
                    if directory_path
                    else args.filename)
        content_lines = []
        print("Enter content lines. Type 'stop' to finish:")
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content_lines.append(line)
        append_content_to_file(filepath, content_lines, timestamp)


if __name__ == "__main__":
    main()
