import os
import sys
from datetime import datetime
from typing import List


def create_directories(dirs: List[str]) -> str:
    """Create directories from provided parts and return full path."""
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def write_to_file(file_path: str, content: List[str]) -> None:
    """Write timestamp and numbered lines to a file."""
    file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a", encoding="utf-8") as target_file:
        if file_exists:
            target_file.write("\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target_file.write(f"{timestamp}\n")
        for line_number, line in enumerate(content, start=1):
            target_file.write(f"{line_number} {line}\n")


def read_content_from_user() -> List[str]:
    """Read multiple lines of input from the user until 'stop'."""
    content: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content.append(line)
    return content


def main() -> None:
    """Main entry point for file or directory creation."""
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py [-d dirs...] [-f filename]")
        return

    dir_parts: List[str] = []
    file_name: str = ""

    if "-d" in args:
        d_index = args.index("-d")
        # Collect directory parts until another flag appears or list ends
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dir_parts.append(arg)

    if "-f" in args:
        f_index = args.index("-f")
        if len(args) > f_index + 1:
            file_name = args[f_index + 1]

    if not dir_parts and not file_name:
        print("Error: no directories or file specified.")
        return

    dir_path = create_directories(dir_parts) if dir_parts else ""

    if not file_name:
        print(f"Directories created: {dir_path or 'current directory'}")
        return

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name
    content = read_content_from_user()
    write_to_file(file_path, content)
    print(f"File created: {file_path}")


if __name__ == "__main__":
    main()
