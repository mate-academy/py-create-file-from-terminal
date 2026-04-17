import os
import sys
import argparse
from datetime import datetime
from typing import List, Optional, Union
from pathlib import Path


def parse_args(argv: List[str]) -> argparse.Namespace:
    """Parse argv, return (dirs: list, file_name: str or None)."""
    dirs = []
    file_name = None
    arg_index = 1
    if len(argv) < 2:
        print("Usage: python script.py [-d dir1 dir2 ...] -f <file_name>")
        sys.exit(1)
    while arg_index < len(argv):
        arg = argv[arg_index]
        if arg == "-d":
            arg_index += 1
            while (
                    arg_index < len(argv) and not
                    argv[arg_index].startswith("-")
            ):
                dirs.append(argv[arg_index])
                arg_index += 1
        elif arg == "-f":
            if arg_index + 1 < len(argv):
                file_name = argv[arg_index + 1]
                arg_index += 2
            else:
                print("Error: -f requires a filename")
                sys.exit(1)
        else:
            arg_index += 1
    return dirs, file_name


def make_dirs(dirs: Union[str, Path]) -> None:
    """Create dirs if provided and return dir_path or empty string."""
    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
    return ""


def collect_content() -> None:
    """Collect lines from input until 'stop' (case-insensitive)."""
    lines = []
    print("Enter content lines (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_content(
        dir_path: str,
        file_name: str,
        content_lines: List[str]
) -> None:
    """Write timestamp and numbered lines to file (append if exists)."""
    if not file_name:
        print("Error: filename is required (-f)")
        sys.exit(1)

    full_path = os.path.join(dir_path, file_name) if dir_path else file_name

    # Check for content to avoid writing empty timestamps
    if not content_lines:
        print("No content to write.")
        return

    # Add a newline separator if the file already exists
    if os.path.exists(full_path):
        with open(full_path, "a", encoding="utf-8") as f:
            f.write("\n")

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(full_path, "a", encoding="utf-8") as f:
        f.write(f"{ts}\n")
        for idx, line in enumerate(content_lines, 1):
            f.write(f"{idx} {line}\n")

    print(f"\nFile saved to: {os.path.abspath(full_path)}")


def main(argv: Optional[List[str]] = None) -> None:
    if argv is None:
        argv = sys.argv
    dirs, file_name = parse_args(argv)
    dir_path = make_dirs(dirs)
    content = collect_content()
    write_content(dir_path, file_name, content)


if __name__ == "__main__":
    main()
