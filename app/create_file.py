from __future__ import annotations
import os
import sys
from datetime import datetime
from typing import LiteralString


def parse_args(argv: list[str]) -> tuple[list[str], str | None]:
    dir_parts = []
    file_name = None
    i = 1
    while i < len(argv):
        if argv[i] == "-d":
            i += 1
            while i < len(argv) and not argv[i].startswith("-"):
                dir_parts.append(argv[i])
                i += 1
        elif argv[i] == "-f":
            i += 1
            if i < len(argv):
                file_name = argv[i]
                i += 1
        else:
            i += 1
    return dir_parts, file_name


def get_content_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(
        file_path: LiteralString | str | bytes,
        lines: list
) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"\n{timestamp}\n")
        for idx, line in enumerate(lines, 1):
            f.write(f"{idx} {line}\n")


def create_file() -> None:
    dir_parts, file_name = parse_args(sys.argv)

    if dir_parts:
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = "."

    if not file_name:
        print("No file name provided. Use -f to specify the file name.")
        return

    file_path = os.path.join(dir_path, file_name)
    lines = get_content_lines()
    write_to_file(file_path, lines)
    print(f"File saved to: {file_path}")


if __name__ == "__main__":
    create_file()
