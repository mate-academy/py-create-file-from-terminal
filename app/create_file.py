import os
import sys
from datetime import datetime
from typing import List


def create_directories(path_parts: List[str]) -> str:
    """Create directories from provided path parts."""
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path


def get_content_from_user() -> List[str]:
    """Prompt user to enter lines until 'stop' is typed."""
    lines: List[str] = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(file_path: str, content: List[str]) -> None:
    """Write timestamp and numbered lines to a file."""
    with open(file_path, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")
        for i, line in enumerate(content, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    """Main entry point to parse arguments and create file."""
    args: List[str] = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py [-d dirs...] -f filename")
        return

    dir_parts: List[str] = []
    file_name: str | None = None

    if "-d" in args:
        d_index = args.index("-d")
        next_flag = (
            args.index("-f") if "-f" in args else len(args)
        )
        dir_parts = args[d_index + 1:next_flag]

    if "-f" in args:
        f_index = args.index("-f")
        if len(args) <= f_index + 1:
            print("Error: file name is missing after -f flag.")
            return
        file_name = args[f_index + 1]

    if not file_name:
        print("Error: you must specify a file with -f flag.")
        return

    directory = create_directories(dir_parts) if dir_parts else "."
    file_path = os.path.join(directory, file_name)

    user_content = get_content_from_user()
    write_to_file(file_path, user_content)
    print(f"File created or updated at: {file_path}")


if __name__ == "__main__":
    main()
