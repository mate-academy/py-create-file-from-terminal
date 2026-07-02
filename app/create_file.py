import os
import sys
from datetime import datetime
from typing import List, Tuple, Optional


def parse_arguments() -> Tuple[Optional[List[str]], Optional[str]]:
    args = sys.argv[1:]
    if not args:
        print("Error: No arguments provided.", file=sys.stderr)
        sys.exit(1)

    dir_components: Optional[List[str]] = None
    filename: Optional[str] = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            # Gather all subsequent elements up to the next known flag
            components = []
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                components.append(args[i])
                i += 1
            if not components:
                print("Error: -d flag requires at least one directory name.",
                      file=sys.stderr)
                sys.exit(1)
            dir_components = components
            continue
        elif args[i] == "-f":
            if i + 1 >= len(args) or args[i + 1].startswith("-"):
                print("Error: -f flag requires a filename argument.",
                      file=sys.stderr)
                sys.exit(1)
            filename = args[i + 1]
            i += 2
        else:
            # Trap any invalid, unexpected, or misspelled flags/arguments
            print(f"Error: Unrecognized argument or flag '{args[i]}'.",
                  file=sys.stderr)
            sys.exit(1)

    return dir_components, filename


def build_paths(
        dir_components: Optional[List[str]],
        filename: Optional[str]
) -> Tuple[str, Optional[str]]:
    """Constructs the directory path and the final target file path strings."""
    directory = os.path.join(*dir_components) if dir_components else ""
    file_path = os.path.join(directory, filename) if filename else None
    return directory, file_path


def create_target_directory(directory: str) -> bool:
    """Creates the target directory structure silently."""
    if not directory:
        return True
    try:
        os.makedirs(directory, exist_ok=True)
        return True
    except Exception:
        return False


def collect_user_input() -> List[str]:
    lines = []
    while True:
        try:
            line = input("Enter content line: ")
            if line.strip() == "stop":
                break
            lines.append(line)
        except (KeyboardInterrupt, EOFError):
            sys.exit(1)
    return lines


def format_file_content(lines: List[str]) -> str:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output_lines = [current_time]

    for index, line in enumerate(lines, start=1):
        output_lines.append(f"{index} {line}")

    return "\n".join(output_lines) + "\n"


def write_to_file(file_path: str, content: str) -> None:
    try:
        parent_dir = os.path.dirname(file_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        file_exists = os.path.exists(file_path)

        with open(file_path, "a", encoding="utf-8") as file:
            if file_exists:
                file.write("\n")
            file.write(content)
    except Exception as e:
        print(f"File Write Error: {e}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    # 1. Strict manual parsing from sys.argv
    dir_components, filename = parse_arguments()
    directory, file_path = build_paths(dir_components, filename)

    # 2. Quietly create directories if -d was explicitly passed
    if dir_components:
        success = create_target_directory(directory)
        if not success:
            sys.exit(1)

    # 3. Guard clause: Exit silently without extra text if only -d was provided
    if not filename or not file_path:
        return

    # 4. Interactive user input session
    lines = collect_user_input()

    # 5. Format layout payload
    formatted_content = format_file_content(lines)

    # 6. Append block to target file path
    write_to_file(file_path, formatted_content)


if __name__ == "__main__":
    main()
