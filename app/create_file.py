#!/usr/bin/env python3
from __future__ import annotations

"""
CLI tool to create directories/files and append timestamped, numbered content.

Flags:
  -d <dir parts...>   Treat subsequent args as nested directory names.
  -f <filename>       Prompt for lines until you enter exactly 'stop'.

Combinations:
  -d ... -f file.txt  Create dirs and write file inside them.
"""

import os
import sys
from datetime import datetime
from typing import List, Optional, Tuple

USAGE = (
    "Usage:\n"
    "  python create_file.py -d dir1 dir2 ...\n"
    "  python create_file.py -f file.txt\n"
    "  python create_file.py -d dir1 dir2 -f file.txt\n\n"
    "Notes:\n"
    "  - After -d pass each directory name as a separate argument.\n"
    "  - After -f pass exactly one filename.\n"
    "  - You will be prompted for lines until you type: stop\n"
)


def parse_args(argv: List[str]) -> Tuple[List[str], Optional[str]]:
    if not argv:
        print(USAGE)
        sys.exit(1)

    dir_parts: List[str] = []
    file_name: Optional[str] = None
    i = 0

    while i < len(argv):
        token = argv[i]
        if token == "-d":
            i += 1
            if i >= len(argv) or argv[i].startswith("-"):
                print("Error: provide at least one directory name after -d.\n")
                print(USAGE)
                sys.exit(1)
            while i < len(argv) and not argv[i].startswith("-"):
                dir_parts.append(argv[i])
                i += 1
            continue

        if token == "-f":
            i += 1
            if i >= len(argv) or argv[i].startswith("-"):
                print("Error: provide a filename after -f.\n")
                print(USAGE)
                sys.exit(1)
            if file_name is not None:
                print("Error: -f specified more than once.\n")
                sys.exit(1)
            file_name = argv[i]
            i += 1
            continue

        print(f"Error: unknown argument '{token}'.\n")
        print(USAGE)
        sys.exit(1)

    if not dir_parts and not file_name:
        print("Error: you must pass -d and/or -f.\n")
        print(USAGE)
        sys.exit(1)

    return dir_parts, file_name


def ensure_dirs(dir_parts: List[str]) -> str:
    """Create nested directories under CWD and return absolute path."""
    if not dir_parts:
        return os.getcwd()
    path = os.path.join(os.getcwd(), *dir_parts)
    os.makedirs(path, exist_ok=True)
    return path


def collect_lines() -> List[str]:
    """Read lines until the user enters exactly 'stop' (case/space sensitive).
    The terminating line 'stop' is not included in the result.
    """
    lines: List[str] = []
    while True:
        try:
            line = input("Enter content line: ")
        except EOFError:
            break
        # exact match only: no strip(), no lower()
        if line == "stop":
            break
        lines.append(line)
    return lines


def append_block(file_path: str, lines: List[str]) -> None:
    """Append a timestamped, numbered block to file_path."""
    if not lines:
        open(file_path, "a", encoding="utf-8").close()
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    need_blank = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a", encoding="utf-8") as f:
        if need_blank:
            f.write("\n")
        f.write(f"{timestamp}\n")
        for idx, text in enumerate(lines, 1):
            f.write(f"{idx} {text}\n")


def main() -> None:
    dir_parts, file_name = parse_args(sys.argv[1:])
    base_dir = ensure_dirs(dir_parts)

    if file_name is None:
        print(f"Created directory: {base_dir}")
        return

    file_path = os.path.join(base_dir, file_name)
    lines = collect_lines()
    append_block(file_path, lines)
    print(f"Written to: {file_path}")


if __name__ == "__main__":
    main()
