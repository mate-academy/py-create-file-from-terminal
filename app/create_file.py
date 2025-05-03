from datetime import datetime
import os
import sys
from typing import LiteralString


def parse_args() -> tuple[list[str], str]:
    args = sys.argv[1:]
    dir_path: list[str] = []
    file_name = ""
    for i in range(len(args)):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_path.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1
    return dir_path, file_name


def create_directory(path: list[str], file_name: str) \
        -> LiteralString | str | bytes:
    full_dir_path = os.path.join(*path) if path else ""
    if full_dir_path:
        os.makedirs(full_dir_path, exist_ok=True)
    if file_name == "":
        return full_dir_path
    return os.path.join(full_dir_path, file_name) \
        if full_dir_path else file_name


def get_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as f:
        f.write(f"\n{timestamp}\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")


def create_file() -> None:
    path, file_name = parse_args()
    full_file_path = create_directory(path, file_name)
    if file_name != "":
        content = get_content()
        write_to_file(full_file_path, content)


if __name__ == "__main__":
    create_file()
