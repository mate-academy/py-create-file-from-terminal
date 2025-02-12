import sys
import os
from datetime import datetime
from pathlib import Path
import argparse


def create_directory(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)
    print(f"Directory created: {path}")


def write_to_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content_lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ").strip()
        if line.lower() == "stop":
            break
        if line:
            content_lines.append(line)

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        separator = "\n\n"
    else:
        separator = ""

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{separator}{timestamp}\n")
        for i, line in enumerate(content_lines, 1):
            f.write(f"{i} {line}\n")

    print(f"File updated: {file_path}")


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py -d [dir1 dir2 ...] -f [filename]")
        sys.exit(1)

    parser = argparse.ArgumentParser(
        description="Create a directory and write to a file."
    )
    parser.add_argument("-d", "--dirs", nargs="+",
                        help="Directories to create.")
    parser.add_argument("-f", "--file", required=True,
                        help="File to write to.")

    args = parser.parse_args()

    full_dir_path = str(Path(*args.dirs)) if args.dirs else ""
    if full_dir_path:
        create_directory(full_dir_path)

    file_path = str(Path(full_dir_path) / args.file)\
        if full_dir_path else args.file
    write_to_file(file_path)


if __name__ == "__main__":
    main()
