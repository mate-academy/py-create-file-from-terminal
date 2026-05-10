import sys
import os
from datetime import datetime
from typing import List, Optional


def parse_dirs(args: List[str]) -> List[str]:
    if "-d" not in args:
        return []

    d_index = args.index("-d")
    dirs: List[str] = []

    for arg in args[d_index + 1:]:
        if arg.startswith("-"):
            break
        dirs.append(arg)

    return dirs


def parse_filename(args: List[str]) -> Optional[str]:
    if "-f" not in args:
        return None

    f_index = args.index("-f")

    if f_index + 1 < len(args):
        return args[f_index + 1]

    return None


def create_directory(dirs: List[str]) -> str:
    if not dirs:
        return ""

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_path: str) -> None:
    dir_name = os.path.dirname(file_path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)

    file_exists = os.path.exists(file_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n\n")

        f.write(timestamp + "\n")

        line_number = 1
        while True:
            line = input("Enter content line:")
            if line == "stop":
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    dirs = parse_dirs(args)
    filename = parse_filename(args)

    path = create_directory(dirs)

    if filename:
        file_path = os.path.join(path, filename) if path else filename
        create_file(file_path)
