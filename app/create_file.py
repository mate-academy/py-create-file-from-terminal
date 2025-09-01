# app/create_file.py

import sys
import os
from datetime import datetime


def parse_args(args: list[str]) -> tuple[str | None, str | None]:
    """Parse command-line arguments and return (dir_path, file_name)."""
    dir_path = None
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        dir_parts = []
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dir_parts.append(arg)
        if not dir_parts:
            print("Error: -d flag requires at least one directory name.")
            sys.exit(1)
        dir_path = os.path.join(*dir_parts)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args) and not args[f_index + 1].startswith("-"):
            file_name = args[f_index + 1]
        else:
            print("Error: -f flag requires a file name.")
            sys.exit(1)

    return dir_path, file_name


def collect_content_lines() -> list[str]:
    """Prompt the user for content lines until 'stop' is entered."""
    lines = []
    counter = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1
    return lines


def format_content_block(lines: list[str]) -> str:
    """Format a content block with timestamp and numbered lines."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timestamp + "\n" + "\n".join(lines) + "\n"


def write_block_to_file(file_path: str, block: str) -> None:
    """Append the block to the file, with separation if file already exists."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    needs_separator = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a", encoding="utf-8") as f:
        if needs_separator:
            f.write("\n")
        f.write(block)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    dir_path, file_name = parse_args(args)

    if not file_name:
        print("Error: -f flag is required to create a file.")
        sys.exit(1)

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    lines = collect_content_lines()
    if not lines:
        print("No lines entered. Nothing was written.")
        sys.exit(0)

    block = format_content_block(lines)
    write_block_to_file(file_path, block)

    print(f"File created/updated at: {file_path}")


if __name__ == "__main__":
    main()
