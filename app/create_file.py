from typing import List
import os
from datetime import datetime
import argparse


def create_directories(path_parts: List[str]) -> str:
    if not path_parts:
        raise ValueError("No directories specified. Please provide at least one directory.")

    path = os.path.join(*path_parts)

    if not os.path.exists(path):
        os.makedirs(path)

    return path


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_content() -> List[str]:
    lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(filepath: str,
                  content_lines: List[str]) -> None:
    timestamp = get_timestamp()

    if os.path.exists(filepath):
        append_write = "a"
    else:
        append_write = "w"

    with open(filepath, append_write) as f:
        if append_write == "a":
            f.write("\n\n")
        f.write(f"{timestamp}\n")

        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")

    print(f"Content successfully written to {filepath}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create file and directories")
    parser.add_argument("-f", "--file",
                        help="File name to create", required=True)
    parser.add_argument("-d", "--dirs",
                        nargs="+", help="Directories to create", required=True)

    args = parser.parse_args()

    file_name = args.file
    directory_parts = args.dirs
    directory_path = create_directories(directory_parts)
    file_path = os.path.join(directory_path, file_name)

    content_lines = get_content()
    write_to_file(file_path, content_lines)

    print(f"File {file_name} created at {directory_path}")


if __name__ == "__main__":
    main()

