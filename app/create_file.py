import sys
import os
from typing import Any
from datetime import datetime


def parse_arguments() -> tuple:
    args = sys.argv[1:]

    if not args or ("-d" not in args and "-f" not in args):
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        sys.exit(1)

    directories = []
    filename = None

    try:
        if "-d" in args:
            d_index = args.index("-d")
            f_index = args.index("-f") if "-f" in args else len(args)
            directories = args[d_index + 1:f_index]

        if "-f" in args:
            f_index = args.index("-f")
            if f_index + 1 < len(args):
                filename = args[f_index + 1]
            else:
                print("Error: -f flag requires a filename")
                sys.exit(1)

    except ValueError as e:
        print(f"Error parsing arguments: {e}")
        sys.exit(1)

    return directories, filename


def get_user_content() -> list:
    lines = []
    print("Enter content lines (type 'stop' to finish):")

    while True:
        try:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            lines.append(line)
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled.")
            sys.exit(1)

    return lines


def format_content_with_timestamp(lines: Any) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = [timestamp]
    formatted.extend(f"{i} {line}" for i, line in enumerate(lines, 1))
    return "\n".join(formatted)


def ensure_directory_exists(path: Any) -> str:
    if path:
        os.makedirs(path, exist_ok=True)
        return path
    return ""


def write_to_file(filepath: Any, content: Any) -> None:
    exists = os.path.exists(filepath)

    with open(filepath, "a" if exists else "w", encoding="utf-8") as f:
        if exists:
            f.write("\n\n")
        f.write(content + "\n")

    action = "appended to" if exists else "created"
    print(f"File {filepath} {action} successfully.")


def main() -> None:
    directories, filename = parse_arguments()

    dir_path = (
        ensure_directory_exists(
            os.path.join(*directories) if directories else ""
        )
    )

    if filename:
        content_lines = get_user_content()
        formatted_content = format_content_with_timestamp(content_lines)

        filepath = os.path.join(dir_path, filename) if dir_path else filename
        write_to_file(filepath, formatted_content)
    elif directories:
        print(f"Directory '{dir_path}' created successfully.")


if __name__ == "__main__":
    main()
