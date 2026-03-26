import os
import sys
from datetime import datetime
from typing import Optional


def parse_args(
        args: list[str]
) -> tuple[list[str], Optional[str]]:
    index = 0
    dirs = []
    file_name = None
    while index < len(args):
        if args[index] == "-d":
            index += 1
            while index < len(args) and not args[index].startswith("-"):
                dirs.append(args[index])
                index += 1
            continue
        if args[index] == "-f":
            index += 1
            if index < len(args) and not args[index].startswith("-"):
                file_name = args[index]
                index += 1
            else:
                file_name = None
                print("No filename after -f")
            continue
        index += 1
    return dirs, file_name


def ensure_dirs(dirs: list[str]) -> str:
    if not dirs:
        return "."
    dirs = [part for part in dirs if part]
    path = os.path.normpath(os.path.join(*dirs))
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"Cannot create directories '{path}': {e}")
        raise
    return path


def collect_lines() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_block(
        dir_path: str,
        file_name: str,
        lines: list[str]
) -> None:
    if dir_path and dir_path != ".":
        full_path = os.path.join(dir_path, file_name)
    else:
        full_path = file_name
    file_exists = os.path.exists(full_path)
    file_non_empty = file_exists and os.path.getsize(full_path) > 0
    with open(full_path, "a", encoding="utf-8") as file:
        if file_non_empty:
            file.write("\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, 1):
            file.write(f"{index} {line}\n")


def create_file() -> None:
    dirs, file_name = parse_args(sys.argv[1:])
    dir_path = ensure_dirs(dirs)
    if file_name is None:
        print("No filename provided")
        return
    lines = collect_lines()
    if not lines:
        return
    write_block(dir_path, file_name, lines)
