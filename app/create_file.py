
import datetime
import os
import sys
from typing import List, Optional, Tuple


def parse_arguments(args: List[str]) -> Tuple[List[str], Optional[str]]:
    directories: List[str] = []
    file_name: Optional[str] = None

    index = 0
    while index < len(args):
        if args[index] == "-d":
            index += 1
            while index < len(args) and not args[index].startswith("-"):
                directories.append(args[index])
                index += 1
        elif args[index] == "-f":
            index += 1
            if index < len(args) and not args[index].startswith("-"):
                file_name = args[index]
            index += 1
        else:
            index += 1

    return directories, file_name


def create_directories(directories: List[str]) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def get_content_lines() -> List[str]:
    lines: List[str] = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def write_to_file(file_path: str, lines: List[str]) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")

        file.write(f"{timestamp}\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


def main() -> None:
    directories, file_name = parse_arguments(sys.argv[1:])

    path = create_directories(directories) if directories else ""

    if file_name:
        full_path = os.path.join(path, file_name) if path else file_name
        lines = get_content_lines()
        write_to_file(full_path, lines)


if __name__ in ("__main__", "<run_path>"):
    main()
