import os
import sys
from datetime import datetime
from typing import List, Tuple


def parse_arguments(args: List[str]) -> Tuple[List[str], str]:
    dir_parts: List[str] = []
    file_name: str = ""
    i: int = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            continue

        if args[i] == "-f" and i + 1 < len(args):
            file_name = args[i + 1]
            i += 2
            continue

        i += 1

    return dir_parts, file_name


def create_directories(dir_parts: List[str]) -> str:
    if not dir_parts:
        return ""

    path: str = os.path.join(*dir_parts)
    os.makedirs(path, exist_ok=True)
    return path


def get_user_content() -> List[str]:
    lines: List[str] = []

    while True:
        line: str = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    return lines


def write_to_file(path: str, lines: List[str]) -> None:
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists: bool = os.path.exists(path)
    file_not_empty: bool = file_exists and os.path.getsize(path) > 0

    with open(path, "a") as file:
        if file_not_empty:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")


def create_file() -> None:
    dir_parts, file_name = parse_arguments(sys.argv[1:])
    directory_path: str = create_directories(dir_parts)

    if not file_name:
        return

    full_path: str = os.path.join(directory_path, file_name)
    content: List[str] = get_user_content()
    write_to_file(full_path, content)


if __name__ == "__main__":
    create_file()
