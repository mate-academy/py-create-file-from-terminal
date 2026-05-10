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

    path: str = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_path: str) -> None:
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines: List[str] = []

    line_number: int = 1

    while True:
        line: str = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(f"{line_number} {line}")
        line_number += 1

    if not content_lines:
        return

    content: str = timestamp + "\n" + "\n".join(content_lines)

    file_exists: bool = os.path.exists(file_path)

    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n\n")
        f.write(content)


def main() -> None:
    args: List[str] = sys.argv[1:]

    dirs: List[str] = parse_dirs(args)
    filename: Optional[str] = parse_filename(args)

    path: str = create_directory(dirs)

    if filename:
        file_path: str = os.path.join(path, filename) if path else filename
        create_file(file_path)


if __name__ == "__main__":
    main()
