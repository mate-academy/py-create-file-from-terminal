import sys
import os
from datetime import datetime
from typing import List


def get_input_lines() -> List[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def format_content(lines: List[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [f"{i + 1} {line}" for i, line in enumerate(lines)]
    return f"{timestamp}\n" + "\n".join(numbered_lines) + "\n"


def parse_args(args: List[str]) -> tuple[list[str], str | None]:
    dirs = []
    filename = None

    # We iterate through args and collect accordingly
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            # Collect all subsequent args that are not flags
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
            else:
                # -f flag present but no filename
                print("Error: -f flag provided but no filename specified.")
                sys.exit(1)
        else:
            # Skip unknown arguments or raise error
            print(f"Warning: Unknown argument {args[i]} skipped.")
            i += 1

    return dirs, filename


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("No arguments provided.")
        return

    dirs, filename = parse_args(args)

    base_path = os.getcwd()
    if dirs:
        base_path = os.path.join(base_path, *dirs)
        os.makedirs(base_path, exist_ok=True)

    if filename:
        file_path = os.path.join(base_path, filename)
        lines = get_input_lines()
        content = format_content(lines)
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n" + content)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
    elif dirs:
        # Only directory creation requested, no file
        pass
    else:
        print("No directory or file specified.")


if __name__ == "__main__":
    main()
