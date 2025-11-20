import sys
import os
from datetime import datetime
from typing import List, Optional


def main() -> None:
    """
    Main function of create_file.py.

    - Reads command-line arguments from sys.argv.
    - Supports flags:
        - -d <dir1 dir2 ...>   → list of directory name parts
        - -f <filename>        → file name to create
    - If both -d and -f are provided,\
    creates directories and a file inside them.
    - Prompts the user for text lines until 'stop' is entered.
    - Writes timestamp + numbered lines into the file.
    - If the file already exists, appends a new block.
    """

    args: List[str] = sys.argv[1:]

    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dir_parts: List[str] = []
    filename: Optional[str] = None

    # Parse flags
    i: int = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            # collect directory parts until next flag
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            continue

        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                print("Error: -f flag requires a file name.")
                return
            continue

        else:
            print(f"Unknown argument: {args[i]}")
            return

    # Build full directory path
    directory_path: str = os.path.join(*dir_parts) if dir_parts else ""

    # Create directory if needed
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    # Ensure a filename was provided
    if not filename:
        print("Error: You must specify a file using -f <filename>")
        return

    # Full file path
    file_path: str = os.path.join(directory_path, filename)

    # Ask user for content
    print()
    lines: List[str] = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line: str = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    # Prepare content block
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block: List[str] = [timestamp] + [f"{i + 1} {text}" for i, text
                                      in enumerate(lines)]
    block_text: str = "\n".join(block) + "\n"

    # Write or append
    mode: str = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n")  # blank line between blocks
        f.write(block_text)

    print(f"\nFile saved at: {file_path}")


if __name__ == "__main__":
    main()
