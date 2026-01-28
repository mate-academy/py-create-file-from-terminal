import os
import sys
from datetime import datetime
from typing import List, Optional, Tuple


def parse_arguments(args: List[str]) \
        -> Tuple[Optional[List[str]], Optional[str]]:

    dir_parts = None
    filename = None
    i: int = 1  # Skip the script name

    while i < len(args):
        if args[i] == "-d":
            dir_parts = []
            i += 1
            # Collect all directory parts until we hit -f or end of args
            while i < len(args) and args[i] != "-f":
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    return dir_parts, filename


def create_directory(directory_path: str) -> None:

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory created: {directory_path}")
    else:
        print(f"Directory already exists: {directory_path}")


def get_user_content() -> List[str]:

    content_lines: List[str] = []
    line_number: int = 1

    print("Enter content line by line. Type 'stop' to finish:")
    while True:
        try:
            line: str = input(f"Enter content line {line_number}: ").strip()
            if line.lower() == "stop":
                break
            content_lines.append(line)
            line_number += 1
        except EOFError:
            break
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            sys.exit(1)

    return content_lines


def format_timestamp() -> str:

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def write_content_to_file(
        filepath: str,
        content_lines: List[str],
        is_new: bool = False
) -> None:

    timestamp: str = format_timestamp()
    mode: str = "a" if os.path.exists(filepath) and not is_new else "w"

    with open(filepath, mode, encoding="utf-8") as file:
        if mode == "a":
            file.write("\n\n")  # Add separation for new content block
        file.write(f"{timestamp}\n")

        for i, line in enumerate(content_lines, 1):
            file.write(f"{i} {line}\n")

    action: str = "Appended to" if mode == "a" and not is_new else "Created"
    print(f"{action} file: {filepath}")


def main() -> None:

    if len(sys.argv) < 2:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        print("Examples:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    # Parse arguments
    dir_parts, filename = parse_arguments(sys.argv)

    # Determine target directory
    target_dir: str = "."
    if dir_parts:
        target_dir = os.path.join(".", *dir_parts)
        create_directory(target_dir)

    # If filename is provided, create file with content
    if filename:
        filepath: str = os.path.join(target_dir, filename)
        content_lines: List[str] = get_user_content()

        if content_lines:
            # Check if file already exists to determine if it's new content
            is_new: bool = not os.path.exists(filepath)
            write_content_to_file(filepath, content_lines, is_new)
        else:
            print("No content provided. File not created.")
    elif dir_parts:
        print(f"Directory structure created: {target_dir}")
    else:
        print("Error: No filename provided. "
              "Use -f flag to specify a filename.")
        sys.exit(1)


if __name__ == "__main__":
    main()
