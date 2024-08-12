import os
import sys
from datetime import datetime


def create_directory(path_ending: list[str]) -> None:
    path = os.path.join(*path_ending)
    os.makedirs(path, exist_ok=True)


def create_file(filename, content_lines) -> None:
    content = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n"

    for i, line in enumerate(content_lines, start=1):
        content += f"{i} {line}\n"

    with open(filename, "a") as file:
        file.write(content)


def main() -> None:
    parts = sys.argv[1:]
    directories = []
    filename = ""

    while parts:
        part = parts.pop(0)
        if part == "-d":
            while parts and parts[0] != "-f":
                directories.append(parts.pop(0))
        elif part == "-f":
            if parts:
                filename = parts.pop(0)

    if directories:
        create_directory(directories)

    if filename:
        filepath = os.path.join(*directories, filename) if directories else filename
        content_lines = []
        while True:
            line = input("Enter content line or type 'stop' to end: ")
            if line == "stop":
                break
            content_lines.append(line)
        create_file(filepath, content_lines)


if __name__ == "__main__":
    main()
