import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    """Create directory if it does not exist."""
    os.makedirs(path, exist_ok=True)


def get_content() -> list[str]:
    """Read content lines from terminal until 'stop' is entered."""
    content_lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content_lines.append(line)

    return content_lines


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    """Write content to file with timestamp and line numbers."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        if file.tell() != 0:
            file.write("\n\n")
        else:
            file.write(f"{timestamp}\n")

        for index, line in enumerate(content_lines, start=1):
            file.write(f"{index} {line}\n")


def main() -> None:
    """Handle command-line arguments and create file."""
    args = sys.argv[1:]

    directories = []
    file_name = None

    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1

            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1

        elif args[i] == "-f":
            i += 1

            if i < len(args) and not args[i].startswith("-"):
                file_name = args[i]
                i += 1

        else:
            i += 1

    if directories:
        dir_path = os.path.join(*directories)
        create_directory(dir_path)
    else:
        dir_path = ""

    if file_name:
        file_path = os.path.join(dir_path, file_name)

        content_lines = get_content()
        write_to_file(file_path, content_lines)


main()
