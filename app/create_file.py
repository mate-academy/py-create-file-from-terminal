import argparse
import os
from datetime import datetime
from typing import List, Optional


TIMESTAMP_FMT = "%Y-%m-%d %H:%M:%S"


def build_dir_path(parts: Optional[List[str]]) -> str:
    if not parts:
        return "."
    return os.path.join(*parts)


def ensure_directories(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def prompt_content_lines() -> List[str]:
    lines: List[str] = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        lines.append(user_input)
    return lines


def write_block(file_path: str, lines: List[str]) -> None:
    file_exists = os.path.exists(file_path)
    has_content = file_exists and os.path.getsize(file_path) > 0

    with open(file_path, mode="a", encoding="utf-8") as handle:
        if has_content:
            handle.write("\n\n")

        timestamp = datetime.now().strftime(TIMESTAMP_FMT)
        handle.write(f"{timestamp}\n")
        for index, text in enumerate(lines, start=1):
            handle.write(f"{index} {text}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Create directories and/or a file, then append a timestamped, "
            "numbered content block read from stdin until 'stop'."
        )
    )
    parser.add_argument(
        "-d",
        "--dirs",
        nargs="+",
        help=(
            "Directory parts. Example: -d dir1 dir2 creates ./dir1/dir2 "
            "relative to the current directory."
        ),
    )
    parser.add_argument(
        "-f",
        "--file",
        help=(
            "File name (e.g., file.txt). "
            "If omitted, only directories are made."
        ),
    )
    args = parser.parse_args()

    dir_path = build_dir_path(args.dirs)
    if args.dirs:
        ensure_directories(dir_path)

    if not args.file:
        return

    file_path = os.path.join(dir_path, args.file)
    lines = prompt_content_lines()
    write_block(file_path, lines)


if __name__ == "__main__":
    main()
