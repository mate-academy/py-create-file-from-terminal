from __future__ import annotations

import os
import sys
from datetime import datetime
from typing import List, Optional


USAGE = (
    "Usage:\n"
    "  python create_file.py -d <dir1> [<dir2> ...]\n"
    "  python create_file.py -f <file.txt>\n"
    "  python create_file.py -d <dir1> [<dir2> ...] -f <file.txt>\n"
)


def build_dir_path(parts: List[str]) -> str:
    """Join directory parts into a platform-independent path."""
    return os.path.join(*parts) if parts else ""


def ensure_dir(path: str) -> None:
    """Create directory tree if a non-empty path is provided."""
    if path:
        os.makedirs(path, exist_ok=True)


def collect_lines() -> List[str]:
    """
    Read lines from stdin until the user types 'stop'.

    The prompt must be exactly 'Enter content line: ' each time.
    """
    lines: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def append_block(file_path: str, lines: List[str]) -> None:
    """
    Append a timestamped, numbered block to file_path.

    Inserts a separating newline if the file already has content.
    """
    parent = os.path.dirname(file_path)
    ensure_dir(parent)

    needs_leading_newline = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a", encoding="utf-8") as fh:
        if needs_leading_newline:
            fh.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fh.write(f"{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            fh.write(f"{idx} {line}\n")


def parse_args(argv: List[str]) -> tuple[List[str], Optional[str]]:
    """
    Very lightweight parser based on sys.argv.

    Returns (dir_parts, file_name).
    """
    dir_parts: List[str] = []
    file_name: Optional[str] = None

    i = 0
    while i < len(argv):
        token = argv[i]
        if token == "-d":
            i += 1
            while i < len(argv) and not argv[i].startswith("-"):
                dir_parts.append(argv[i])
                i += 1
            continue
        if token == "-f":
            i += 1
            if i >= len(argv) or argv[i].startswith("-"):
                print(USAGE)
                sys.exit(1)
            file_name = argv[i]
            i += 1
            continue
        print(USAGE)
        sys.exit(1)
    return dir_parts, file_name


def main() -> None:
    if len(sys.argv) <= 1:
        print(USAGE)
        sys.exit(1)

    args = sys.argv[1:]
    dir_parts, file_name = parse_args(args)

    dir_path = build_dir_path(dir_parts)
    ensure_dir(dir_path)

    if file_name is None:
        return

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    lines = collect_lines()
    append_block(file_path, lines)


if __name__ == "__main__":
    main()
