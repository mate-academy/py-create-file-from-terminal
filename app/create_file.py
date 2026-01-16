#!/usr/bin/env python3
from __future__ import annotations

import os
import sys
from datetime import datetime
from typing import List, Tuple, Optional


def parse_args(argv: List[str]) -> Tuple[List[str], Optional[str]]:

    dirs: List[str] = []
    file_name: Optional[str] = None

    i = 1
    while i < len(argv):
        arg = argv[i]

        if arg in ("-d", "--dir"):
            i += 1
            while i < len(argv) and not argv[i].startswith("-"):
                dirs.append(argv[i])
                i += 1

        elif arg in ("-f", "--file"):
            if i + 1 >= len(argv):
                raise ValueError("Missing file name after -f/--file")
            file_name = argv[i + 1]
            i += 2

        else:
            raise ValueError(f"Unknown argument: {arg}")

    return dirs, file_name


def read_content() -> List[str]:

    lines: List[str] = []

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    return lines


def format_block(lines: List[str]) -> str:

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_lines = [
        f"{index} {line}"
        for index, line in enumerate(lines, start=1)
    ]

    return "\n".join(
        [timestamp, *formatted_lines, ""]
    )


def main() -> None:
    try:
        dirs, file_name = parse_args(sys.argv)
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)

    base_path = os.getcwd()

    if dirs:
        base_path = os.path.join(base_path, *dirs)
        os.makedirs(base_path, exist_ok=True)

    if not file_name:
        return

    file_path = os.path.join(base_path, file_name)

    content_lines = read_content()
    if not content_lines:
        return

    block = format_block(content_lines)

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(block)


if __name__ == "__main__":
    main()
