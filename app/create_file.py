import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    """
    Join list of into a path cross-platform
    """
    return os.path.join(*directories)


def make_directories(path: str) -> None:
    """
    Create directories if they do not exist.
    """
    os.makedirs(path, exist_ok=True)


def collect_content_lines() -> list:
    """
    Prompt the user for content lines until 'stop; is entered.
    """
    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input.strip().lower() == "stop":
            break
        lines.append(user_input)
    return lines


def write_content_to_file(filepath: str, lines: list) -> None:
    """
    Write timestamp and numbered lines to file.
    Append if the dile exists.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            file.write(f"{idx} {line}\n")
        file.write("\n")


def main() -> None:
    args = sys.argv[1:]
    directory_path = []
    file_name = None

    i = 0
    while i < len(*args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directory_path.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            # Ignore unknown arguments
            i += 1

    # Only files
    if file_name and not directory_path:
        path = file_name
        lines = collect_content_lines()
        write_content_to_file(path, lines)
        print(f"File created/updated: {path}")

    if directory_path and file_name:
        dir_path = create_path(directory_path)
        make_directories((dir_path))
        path = os.path.join(dir_path, file_name)
        lines = collect_content_lines()
        write_content_to_file(path, lines)
        print(f"Directory and file created/updated: {path}")
        return

    print("Usage:")
    print(" python create_file.py -d dir1 dir2")
    print(" python create_file.py -f filename.txt")
    print(" python create_file.py -d dir1 dir2 -f filename.txt")


if __name__ == "__main__":
    main()
