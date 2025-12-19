import os
import sys
from datetime import datetime
from typing import List, Optional


def create_directories(parts: List[str]) -> str:
    if not parts:
        return ""

    path = os.path.join(*parts)
    os.makedirs(path, exist_ok=True)
    return path


def get_user_content() -> List[str]:
    lines: List[str] = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    return lines


def write_to_file(
    folder_path: str,
    file_name: str,
    content: List[str],
) -> None:
    full_path = os.path.join(folder_path, file_name)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(full_path)

    with open(full_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for index, line in enumerate(content, start=1):
            file.write(f"{index} {line}\n")


def parse_arguments(
    args: List[str],
) -> tuple[List[str], Optional[str]]:
    directory_parts: List[str] = []
    file_name: Optional[str] = None
    mode: Optional[str] = None

    for arg in args:
        if arg == "-d":
            mode = "dir"
            continue

        if arg == "-f":
            mode = "file"
            continue

        if mode == "dir":
            directory_parts.append(arg)
        elif mode == "file" and file_name is None:
            file_name = arg

    return directory_parts, file_name


def main() -> None:
    directory_parts, file_name = parse_arguments(sys.argv[1:])

    folder_path = create_directories(directory_parts)

    if file_name is None:
        return

    content = get_user_content()
    write_to_file(folder_path, file_name, content)

