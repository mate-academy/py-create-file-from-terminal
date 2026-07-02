import argparse
from datetime import datetime
import os
import sys
from typing import List, Tuple, Optional


def parse_arguments() -> Tuple[Optional[List[str]], Optional[str]]:
    """Parses command-line arguments safely."""
    parser = argparse.ArgumentParser(
        description="Create directories and/or files with content."
    )
    parser.add_argument("-d", nargs="+", default=None, metavar="DIR")
    parser.add_argument("-f", default=None, metavar="FILENAME")
    return parser.parse_known_args()


def build_paths(
        dir_components: Optional[List[str]],
        filename: Optional[str]
) -> Tuple[str, Optional[str]]:
    """Constructs the directory path and the final target file path."""
    # os.path.join(*dir_components) unfolds ['dir1', 'dir2'] into 'dir1/dir2'
    directory = os.path.join(*dir_components) if dir_components else ""
    file_path = os.path.join(directory, filename) if filename else None
    return directory, file_path


def create_target_directory(directory: str) -> bool:
    """Creates the target directory structure. Crucial to prevent Errno 2."""
    if not directory:
        return True
    try:
        # exist_ok=True prevents errors if the directory already exists
        os.makedirs(directory, exist_ok=True)
        return True
    except Exception as e:
        print(f"OS Error creating directory structure '{directory}': {e}")
        return False


def collect_user_input() -> List[str]:
    """Collects lines of input from the terminal until 'stop' is entered."""
    lines = []
    while True:
        try:
            line = input("Enter content line: ")
            if line.strip().lower() == "stop":
                break
            lines.append(line)
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled by user.")
            sys.exit(1)
    return lines


def format_file_content(lines: List[str]) -> str:
    """Formats raw input lines with a current
    timestamp header and line numbering."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_lines = [current_time]

    for index, line in enumerate(lines, start=1):
        output_lines.append(f"{index} {line}")

    return "\n".join(output_lines) + "\n"


def write_to_file(file_path: str, content: str) -> None:
    """Writes content safely, ensuring parent folders exist."""
    try:
        # Double check: ensure the parent directory exists right before opening
        parent_dir = os.path.dirname(file_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        file_exists = os.path.exists(file_path)

        with open(file_path, "a", encoding="utf-8") as file:
            if file_exists:
                file.write("\n")  # Blank line separator for new blocks
            file.write(content)

        print(f"Successfully updated file: {file_path}")
    except Exception as e:
        print(f"File Write Error: {e}")


def main() -> None:
    # 1. Parse arguments
    args, unknown = parse_arguments()

    # 2. Build paths
    directory, file_path = build_paths(args.d, args.f)

    # 3. Create directory first (if -d was provided)
    if args.d:
        if not create_target_directory(directory):
            print("Skipping file creation due to directory failure.")
            sys.exit(1)

    # 4. If -f wasn't provided, stop here (directory is already made!)
    if not args.f:
        print(f"Directory structure verified/created: "
              f"{directory if directory else '.'}")
        return

    # 5. Gather inputs, format, and safely write to file
    lines = collect_user_input()
    formatted_content = format_file_content(lines)
    write_to_file(file_path, formatted_content)


if __name__ == "__main__":
    main()
