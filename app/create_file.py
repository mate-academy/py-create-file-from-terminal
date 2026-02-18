import os
import sys
from datetime import datetime


def create_path(directories: list[str]) -> str:
    """Join directories into valid path and create them if needed."""
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def get_content_lines() -> list[str]:
    """Collect content lines from user input until 'stop' is entered."""
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_content(file_path: str, lines: list[str]) -> None:
    """Write timestamp and numbered lines to the file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"\n{timestamp}\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    if "-d" not in args and "-f" not in args:
        print("Usage: -d dir1 dir2 ... -f filename OR -f filename")
        return

    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_parts = args[d_index + 1:f_index]
        else:
            dir_parts = args[d_index + 1:]
        if dir_parts:
            dir_path = create_path(dir_parts)

    if "-f" in args:
        f_index = args.index("-f")
        try:
            file_name = args[f_index + 1]
        except IndexError:
            print("Error: file name is missing after -f")
            return

        full_file_path = (
            os.path.join(dir_path, file_name) if dir_path else file_name
        )

        content_lines = get_content_lines()
        write_content(full_file_path, content_lines)

        print(f"File saved at: {full_file_path}")
