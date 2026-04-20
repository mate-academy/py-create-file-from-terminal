import sys
import os
from datetime import datetime
from typing import List, Tuple


def parse_arguments(arguments: List[str]) -> Tuple[List[str], str | None]:
    directories: List[str] = []
    file_name: str | None = None

    index = 1
    while index < len(arguments):
        if arguments[index] == "-d":
            index += 1
            while (
                index < len(arguments)
                and not arguments[index].startswith("-")
            ):
                directories.append(arguments[index])
                index += 1
        elif arguments[index] == "-f":
            index += 1
            if index < len(arguments):
                file_name = arguments[index]
                index += 1
        else:
            index += 1

    return directories, file_name


def read_file_content() -> List[str]:
    lines: List[str] = []
    while True:
        line: str = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_content_to_file(file_path: str, lines: List[str]) -> None:
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists_and_not_empty: bool = (
        os.path.exists(file_path)
        and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a", encoding="utf-8") as output_file:
        if file_exists_and_not_empty:
            output_file.write("\n")

        output_file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            output_file.write(f"{index} {line}\n")


def main() -> None:
    directories, file_name = parse_arguments(sys.argv)

    base_path: str = os.getcwd()

    if directories:
        base_path = os.path.join(base_path, *directories)
        os.makedirs(base_path, exist_ok=True)

    if file_name:
        file_path: str = os.path.join(base_path, file_name)
        lines: List[str] = read_file_content()
        write_content_to_file(file_path, lines)
