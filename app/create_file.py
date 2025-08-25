import sys
import os
from typing import List, Tuple, Optional
from datetime import datetime


def parse_args(argv: List[str]) -> Tuple[List[str], Optional[str]]:
    """
    Parse flags from argv (supports -d and -f in any order).
    -d collects all subsequent non-flag tokens as path parts until next flag or end.
    -f takes exactly one token (file name).
    Returns (dir_parts, file_name).
    """
    dir_parts: List[str] = []
    file_name: Optional[str] = None

    i = 1
    while i < len(argv):
        token = argv[i]
        if token == "-d":
            i += 1
            # Collect path segments until next flag or end
            while i < len(argv) and not argv[i].startswith("-"):
                dir_parts.append(argv[i])
                i += 1
            continue
        elif token == "-f":
            i += 1
            if i >= len(argv) or argv[i].startswith("-"):
                raise ValueError("Flag -f requires a file name right after it.")
            file_name = argv[i]
            i += 1
            continue
        else:
            raise ValueError(f"Unknown flag or argument: {token}")
    return dir_parts, file_name


def ensure_directory(dir_parts: List[str]) -> Optional[str]:
    """Create directory from parts (if provided). Return the created path or None."""
    if not dir_parts:
        return None
    dir_path = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory created: {dir_path}")
    return dir_path


def prompt_lines() -> List[str]:
    """Prompt for content lines until user types 'stop' (exactly)."""
    lines: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def format_block(lines: List[str]) -> str:
    """Return a text block: timestamp line, then numbered lines, ending with newline."""
    ts: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered = [f"{i+1} {line}" for i, line in enumerate(lines)]
    return f"{ts}\n" + "\n".join(numbered) + "\n"


def write_block(file_path: str, block: str) -> None:
    """Append a block to file, inserting a blank line if file already has content."""
    add_blank = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a", encoding="utf-8") as f:
        if add_blank:
            f.write("\n")
        f.write(block)
    print(f"File created/updated: {file_path}")


def main() -> None:
    try:
        dir_parts, file_name = parse_args(sys.argv)
    except ValueError as e:
        print(f"Error: {e}")
        print("Usage examples:")
        print("  python create_file.py -d dir1 dir2")
        print("  python create_file.py -f file.txt")
        print("  python create_file.py -d dir1 dir2 -f file.txt")
        sys.exit(1)

    # If only -d → create directory and exit.
    created_dir = ensure_directory(dir_parts)
    if file_name is None:
        if not dir_parts:
            print("You must provide at least one flag: -d or -f")
            sys.exit(1)
        return

    # If -f present → create (or append to) file, possibly inside created directory.
    file_path = file_name if not created_dir else os.path.join(created_dir, file_name)

    print("(Type lines, then 'stop' to finish.)")
    lines = prompt_lines()
    # Always write a timestamp block; if no lines, still write timestamp only.
    block = format_block(lines)
    write_block(file_path, block)


if __name__ == "__main__":
    main()