import os
import sys
from datetime import datetime


def get_arguments() -> tuple[list[str], str | None]:
    args = sys.argv
    directories = []
    file_name = None

    if "-d" in args:
        start = args.index("-d") + 1
        end = len(args)
        if "-f" in args and args.index("-f") > start:
            end = args.index("-f")
        directories = args[start:end]

    if "-f" in args and args.index("-f") + 1 < len(args):
        file_name = args[args.index("-f") + 1]

    return directories, file_name


def create_directories(directories: list[str]) -> str:
    if not directories:
        return ""
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def read_content_lines() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, lines: list[str]) -> None:
    file_exists = os.path.exists(file_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as source_file:
        if file_exists:
            source_file.write("\n")
        source_file.write(f"{timestamp}\n")
        for number, line in enumerate(lines, start=1):
            source_file.write(f"{number} {line}\n")


def main() -> None:
    directories, file_name = get_arguments()

    if not directories and not file_name:
        print("Usage: python create_file.py [-d dir1 dir2] [-f file.txt]")
        return

    directory_path = create_directories(directories)

    if file_name:
        file_path = os.path.join(directory_path, file_name)
        lines = read_content_lines()
        write_to_file(file_path, lines)


main()
