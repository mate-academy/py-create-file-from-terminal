from __future__ import annotations

import os
import sys
from datetime import datetime


def create_path(directories: list[str]) -> str:
    """Return a joined path created from directory parts."""
    return os.path.join(*directories)


def get_content_lines() -> list[str]:
    """Read user input lines until 'stop' is entered."""
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, lines: list[str]) -> None:
    """Write timestamp and numbered lines to a file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"\n{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            file.write(f"{idx} {line}\n")


def main() -> None:
    """Parse CLI flags and create directories/files with content."""
    args = sys.argv[1:]

    if "-d" not in args and "-f" not in args:
        print("Usage: python create_file.py -d <dirs> -f <filename>")
        sys.exit(1)

    path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d") + 1
        next_flag = args.index("-f") if "-f" in args else len(args)
        dirs = args[d_index:next_flag]
        path = create_path(dirs)
        os.makedirs(path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f") + 1
        file_name = args[f_index]
        file_path = os.path.join(path, file_name) if path else file_name

        content_lines = get_content_lines()
        write_to_file(file_path, content_lines)
        print(f"File created/updated at: {file_path}")


if __name__ == "__main__":
    main()
