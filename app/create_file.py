import os
import sys
from datetime import datetime


def create_new_file(path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"=== {timestamp} ===\n\n")


def append_block(path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"=== {timestamp} ===\n")
        for i, text in enumerate(lines, start=1):
            f.write(f"{i}. {text}\n")
        f.write("\n")


def parse_directory_args(args: list[str]) -> str | None:
    if "-d" not in args:
        return None

    start = args.index("-d") + 1
    dir_parts = []

    for i in range(start, len(args)):
        if args[i].startswith("-"):
            break
        dir_parts.append(args[i])

    if not dir_parts:
        print("Error: -d flag requires a directory path.")
        sys.exit(1)

    return os.path.join(*dir_parts)


def create_file() -> None:
    args = sys.argv

    directory = parse_directory_args(args)

    file_name = None
    if "-f" in args:
        try:
            file_name = args[args.index("-f") + 1]
        except IndexError:
            print("Error: -f flag requires a file name.")
            sys.exit(1)

    if directory and file_name:
        os.makedirs(directory, exist_ok=True)
        full_path = os.path.join(directory, file_name)

    elif file_name:
        full_path = file_name

    elif directory:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory created: {directory}")
        return

    else:
        print("Usage: python create_file.py -d <dir> -f <file>")
        return

    if not os.path.exists(full_path):
        create_new_file(full_path)
        print(f"File created: {full_path}")
    else:
        print(f"Appending to existing file: {full_path}")

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    append_block(full_path, lines)
    print(f"Content added to {full_path}")


if __name__ == "__main__":
    create_file()
