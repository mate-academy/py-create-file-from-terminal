import os
import sys
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    dirs = []
    file_name = None

    index = 0
    while index < len(args):
        if args[index] == "-d":
            index += 1
            while index < len(args) and args[index] != "-f":
                dirs.append(args[index])
                index += 1
        elif args[index] == "-f":
            index += 1
            if index < len(args):
                file_name = args[index]
                index += 1
        else:
            index += 1

    return dirs, file_name


def read_content_lines() -> list:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def build_entry(content_lines: list) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = timestamp + "\n"
    for index, line in enumerate(content_lines, start=1):
        entry += f"{index} {line}\n"
    return entry


def main() -> None:
    dirs, file_name = parse_arguments(sys.argv[1:])

    directory_path = os.path.join(*dirs) if dirs else ""
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    if file_name:
        full_path = (
            os.path.join(directory_path, file_name)
            if directory_path else file_name
        )

        content_lines = read_content_lines()
        entry = build_entry(content_lines)
        file_exists = os.path.exists(full_path)

        with open(full_path, "a") as file:
            if file_exists:
                file.write("\n")
            file.write(entry)


main()
