import sys
import os
from datetime import datetime


def parse_args(argv: None) -> None:
    """
    Parse sys.argv manually to extract -d and -f flag values.
    Returns (dir_parts, filename) where either can be None.
    """
    dir_parts = None
    filename = None

    i = 1
    while i < len(argv):
        if argv[i] == "-d":
            dir_parts = []
            i += 1
            while i < len(argv) and not argv[i].startswith("-"):
                dir_parts.append(argv[i])
                i += 1
        elif argv[i] == "-f":
            i += 1
            if i < len(argv):
                filename = argv[i]
                i += 1
            else:
                print("Error: -f flag requires a filename argument.")
                sys.exit(1)
        else:
            print(f"Error: Unknown flag '{argv[i]}'.")
            sys.exit(1)

    return dir_parts, filename


def collect_content() -> None:
    """
    Interactively collect lines from the user until they type 'stop'.
    Returns formatted content block (timestamp + numbered lines).
    """
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    block = timestamp + "\n"
    for number, text in enumerate(lines, start=1):
        block += f"{number} {text}\n"

    return block


def create_directory(dir_parts: None) -> None:
    """Join dir_parts into a path and create it
     (including any missing parents)."""
    path = os.path.join(*dir_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")
    return path


def create_file(directory: None, filename: None) -> None:
    """
    Collect content from user and write/append it to the file.
    If the file already exists, appends a blank line then the new block.
    """
    filepath = os.path.join(directory, filename)

    already_exists = os.path.isfile(filepath)

    content_block = collect_content()

    with open(filepath, "a") as f:
        if already_exists:
            f.write("\n")
        f.write(content_block)

    print(f"File saved: {filepath}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    dir_parts, filename = parse_args(sys.argv)

    if dir_parts and filename:
        directory = create_directory(dir_parts)
        create_file(directory, filename)

    elif dir_parts:
        create_directory(dir_parts)

    elif filename:
        create_file(".", filename)

    else:
        print("Error: provide at least one flag: -d or -f")
        sys.exit(1)


main()
