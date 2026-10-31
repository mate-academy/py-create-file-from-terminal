import datetime
import os
import sys
from typing import List, Optional, Tuple


def parse_arguments(args: List[str]) -> Tuple[List[str], Optional[str]]:
    directories: List[str] = []
    file_name: Optional[str] = None
    i = 1
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1
    return directories, file_name


def collect_content_lines() -> List[str]:
    lines: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, lines: List[str]) -> None:
    timestamp = datetime.datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    file_exists = os.path.exists(file_path)
    is_not_empty = file_exists and os.path.getsize(file_path) > 0

    with open(file_path, "a", encoding="utf-8") as target_file:
        if is_not_empty:
            target_file.write("\n")
        target_file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            target_file.write(f"{index} {line}\n")


def main() -> None:
    directories, file_name = parse_arguments(sys.argv)

    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        if directories:
            file_path = os.path.join(*(directories + [file_name]))
        else:
            file_path = file_name

        lines = collect_content_lines()
        write_to_file(file_path, lines)


if __name__ == "__main__":
    main()
