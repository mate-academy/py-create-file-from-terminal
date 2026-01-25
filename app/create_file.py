import sys
import os
from datetime import datetime
from typing import List, Tuple, Optional


def parse_arguments(argv: List[str]) -> Tuple[List[str], Optional[str]]:
    directories: List[str] = []
    filename: Optional[str] = None

    index = 1
    while index < len(argv):
        if argv[index] == "-d":
            index += 1
            while index < len(argv) and not argv[index].startswith("-"):
                directories.append(argv[index])
                index += 1
        elif argv[index] == "-f":
            index += 1
            if index < len(argv):
                filename = argv[index]
                index += 1
        else:
            index += 1

    return directories, filename


def read_content() -> List[str]:
    lines: List[str] = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def format_content(lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result: List[str] = [timestamp]

    for number, line in enumerate(lines, start=1):
        result.append(f"{number} {line}")

    return "\n".join(result) + "\n\n"


def main() -> None:
    directories, filename = parse_arguments(sys.argv)

    base_path = os.getcwd()

    if directories:
        base_path = os.path.join(base_path, *directories)
        os.makedirs(base_path, exist_ok=True)

    if filename is None:
        return

    file_path = os.path.join(base_path, filename)
    content_lines = read_content()
    formatted_content = format_content(content_lines)

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(formatted_content)


if __name__ == "__main__":
    main()
