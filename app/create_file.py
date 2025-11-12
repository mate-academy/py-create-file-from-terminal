#!/usr/bin/env python3
import sys
import os
from datetime import datetime


def create_directories(dir_parts):
    """Create directories based on parts of the path."""
    dir_path = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def get_content_from_user():
    """Prompt the user to input lines until 'stop' is entered."""
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path, lines):
    """Write timestamp and numbered lines to the file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}\n")
        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")
        file.write("\n")
    print(f"File created/updated at: {file_path}")


def main():
    """Main entry point of the script."""
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        sys.exit(1)

    dir_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        for item in args[d_index + 1:]:
            if item == "-f":
                break
            dir_parts.append(item)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            print("Error: Missing file name after -f flag.")
            sys.exit(1)

    if dir_parts and file_name:
        dir_path = create_directories(dir_parts)
        file_path = os.path.join(dir_path, file_name)
        lines = get_content_from_user()
        write_to_file(file_path, lines)

    elif dir_parts and not file_name:
        create_directories(dir_parts)
        print(f"Directory created: {os.path.join(*dir_parts)}")

    elif file_name and not dir_parts:
        lines = get_content_from_user()
        write_to_file(file_name, lines)

    else:
        print("Error: Invalid usage. Please provide -d or -f flag.")
        sys.exit(1)


if __name__ == "__main__":
    main()
