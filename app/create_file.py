import sys
import os
from datetime import datetime
from typing import List, Optional


def create_directory(path: str) -> None:
    """Creates a directory at the specified path."""
    if os.path.exists(path):
        print(f"Directory '{path}' already exists. Exiting.")
        return
    try:
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created successfully.")
    except Exception as e:
        print(f"Error creating directory: {e}")


def create_file(file_path: str) -> None:
    """Creates or appends content to a file at the specified path."""
    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists. Exiting.")
        return

    lines: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"{timestamp}\n" + "\n".join(f"{i + 1} {line}"
                                           for i, line in enumerate(lines))

    with open(file_path, "w") as file:
        file.write(content)

    print(f"File '{file_path}' created successfully.")


def parse_arguments(args: List[str]) -> Optional[tuple]:
    """Parses command-line arguments."""
    if not args or "-d" not in args and "-f" not in args:
        print("Error: Missing required flags '-d' and/or '-f'.")
        return None

    if "-d" in args and "-f" in args and args.index("-f") < args.index("-d"):
        print("Error: '-f' flag cannot come before '-d' flag.")
        return None

    path = file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        path_components = args[d_index + 1:args.index("-f")]\
            if "-f" in args else args[d_index + 1:]
        path = os.path.join(*path_components)

    if "-f" in args:
        f_index = args.index("-f")
        if len(args) <= f_index + 1:
            print("Error: Missing file name after '-f' flag.")
            return None
        file_name = args[f_index + 1]

    return path, file_name


def main() -> None:
    """Main function to handle command-line arguments
     and create directories or files."""
    parsed_args = parse_arguments(sys.argv[1:])
    if parsed_args is None:
        return

    path, file_name = parsed_args

    if path:
        create_directory(path)

    if file_name:
        file_path = os.path.join(path, file_name) if path else file_name
        create_file(file_path)


if __name__ == "__main__":
    main()
