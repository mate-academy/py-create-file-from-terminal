import os
import sys
from datetime import datetime
from typing import Optional


def parse_arguments(args: list[str]) -> tuple[list[str], Optional[str]]:
    """
    Parse CLI arguments and return directory parts and file name.
    """
    dir_parts: list[str] = []
    file_name: Optional[str] = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in {"-d", "-f"}:
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1

    return dir_parts, file_name


def read_content() -> list[str]:
    """
    Read content lines from user until 'stop'.
    """
    lines: list[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: list[str]) -> str:
    """
    Add timestamp and line numbers.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{idx + 1} {line}" for idx, line in enumerate(lines)]
    return timestamp + "\n" + "\n".join(numbered_lines) + "\n\n"


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dir_parts, file_name = parse_arguments(args)

    base_path = os.getcwd()

    # Create directory if needed
    if dir_parts:
        dir_path = os.path.join(base_path, *dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = base_path

    # If only -d flag → stop after creating directories
    if file_name is None:
        print(f"Directories created: {dir_path}")
        return

    file_path = os.path.join(dir_path, file_name)

    lines = read_content()
    if not lines:
        print("No content provided.")
        return

    content_block = format_content(lines)

    # Append or create file
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content_block)

    print(f"File created/updated: {file_path}")


if __name__ == "__main__":
    main()
# write your code here
