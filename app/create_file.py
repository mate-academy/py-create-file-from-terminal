import sys
import os
from datetime import datetime
from typing import List, Tuple, Optional


def parse_arguments() -> Tuple[List[str], Optional[str]]:
    """
    Parse command line arguments.

    Returns:
        Tuple containing:
        - list of directory parts
        - file name (or None)
    """

    args: List[str] = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        sys.exit(1)

    dir_parts: List[str] = []
    file_name: Optional[str] = None

    i: int = 0

    while i < len(args):

        if args[i] == "-d":
            i += 1

            while i < len(args) and args[i] not in ("-d", "-f"):
                dir_parts.append(args[i])
                i += 1

            continue

        if args[i] == "-f":
            i += 1

            if i < len(args):
                file_name = args[i]
                i += 1
            else:
                print("Error: No file name after -f")
                sys.exit(1)

            continue

        i += 1

    return dir_parts, file_name


def create_directory_path(dir_parts: List[str]) -> str:
    """
    Create directory path.

    Returns:
        Full directory path.
    """

    current_path: str = os.getcwd()

    if dir_parts:
        dir_path: str = os.path.join(current_path, *dir_parts)

        os.makedirs(dir_path, exist_ok=True)

        return dir_path

    return current_path


def get_user_lines() -> List[str]:
    """
    Read user input lines until 'stop'.
    """

    lines: List[str] = []

    while True:
        user_input: str = input("Enter content line: ")

        if user_input == "stop":
            break

        lines.append(user_input)

    return lines


def format_content(
    lines: List[str],
    file_exists: bool,
) -> List[str]:
    """
    Format content with timestamp and numbering.
    """

    now: datetime = datetime.now()

    timestamp: str = now.strftime("%Y-%m-%d %H:%M:%S")

    content: List[str] = []

    if file_exists:
        content.append("\n")

    content.append(timestamp + "\n")

    for i, line in enumerate(lines, start=1):
        content.append(f"{i} {line}\n")

    return content


def write_file(
    directory: str,
    file_name: str,
) -> None:
    """
    Write content into file.
    """

    file_path: str = os.path.join(directory, file_name)

    lines: List[str] = get_user_lines()

    file_exists: bool = os.path.exists(file_path)

    content: List[str] = format_content(lines, file_exists)

    with open(file_path, "a", encoding="utf-8") as f:
        f.writelines(content)

    print(f"File created/updated at: {file_path}")


def main() -> None:
    """
    Main program execution.
    """

    dir_parts, file_name = parse_arguments()

    directory: str = create_directory_path(dir_parts)

    if file_name:
        write_file(directory, file_name)


if __name__ == "__main__":
    main()
