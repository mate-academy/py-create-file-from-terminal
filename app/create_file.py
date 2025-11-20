import sys
import os
from datetime import datetime
from typing import List, Optional, Tuple


def parse_arguments(args: List[str]) -> Tuple[List[str], Optional[str]]:
    """
    Parse command-line arguments into directory parts and optional filename.

    Args:
        args (List[str]): List of arguments from sys.argv[1:].

    Returns:
        Tuple[List[str], Optional[str]]:
            - List of directory name components
            - Filename if provided, else None
    """
    dir_parts: List[str] = []
    filename: Optional[str] = None

    arg_index = 0
    while arg_index < len(args):

        if args[arg_index] == "-d":
            arg_index += 1
            while (arg_index < len(args)
                   and not args[arg_index].startswith("-")):
                dir_parts.append(args[arg_index])
                arg_index += 1
            continue

        elif args[arg_index] == "-f":
            arg_index += 1
            if arg_index < len(args):
                filename = args[arg_index]
                arg_index += 1
            else:
                print("Error: -f flag requires a filename.")
                sys.exit(1)
            continue

        else:
            print(f"Unknown argument: {args[arg_index]}")
            sys.exit(1)

    return dir_parts, filename


def create_directories(dir_parts: List[str]) -> str:
    """
    Create a directory path based on the list of directory components.

    Args:
        dir_parts (List[str]): Directory name parts.

    Returns:
        str: The created directory path
         (or empty string if no directories used).
    """
    if not dir_parts:
        return ""

    directory_path = os.path.join(*dir_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def collect_user_input() -> List[str]:
    """
    Collect user input lines until 'stop' is entered.

    Returns:
        List[str]: List of user-entered lines.
    """
    print("Enter content line (type 'stop' to finish):")
    collected_lines: List[str] = []

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        collected_lines.append(line)

    return collected_lines


def write_content_to_file(file_path: str, lines: List[str]) -> None:
    """
    Write timestamped and numbered lines to a file. Append if file exists.

    Args:
        file_path (str): Path to the file being written.
        lines (List[str]): User input lines.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    block = [timestamp] + [
        f"{line_number + 1} {text}"
        for line_number, text in enumerate(lines)
    ]

    block_text = "\n".join(block) + "\n"

    file_exists = os.path.exists(file_path)
    mode = "a" if file_exists else "w"

    with open(file_path, mode, encoding="utf-8") as output_file:
        if file_exists:
            output_file.write("\n")  # Blank line between blocks
        output_file.write(block_text)

    print(f"\nFile saved at: {file_path}")


def main() -> None:
    """
    Main entry point of the program.
    Handles argument parsing, directory creation,
     file writing, and input collection.
    """
    args = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dir_parts, filename = parse_arguments(args)

    # Create directories if needed
    directory_path = create_directories(dir_parts)

    # If only -d provided → create directories and exit (fixed requirement)
    if dir_parts and filename is None:
        print(f"Directory created: {directory_path}")
        return

    # -f is required if user wants to create a file
    if filename is None:
        print("Error: Missing filename. Use -f <filename>.")
        return

    # Build full path to the file
    file_path = os.path.join(directory_path, filename)

    # Collect user input for file content
    user_lines = collect_user_input()

    # Write content to file
    write_content_to_file(file_path, user_lines)


if __name__ == "__main__":
    main()
