import sys
import os
from datetime import datetime
from typing import List, Optional


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

    dirs: List[str] = []
    filename: Optional[str] = None

    if "-d" in args:
        d_index: int = args.index("-d")

        if "-f" in args:
            f_index: int = args.index("-f")
            dirs = args[d_index + 1:f_index]
        else:
            dirs = args[d_index + 1:]

    if "-f" in args:
        f_index: int = args.index("-f")
        try:
            filename = args[f_index + 1]
        except IndexError:
            return

    path: str = create_directory(dirs)

    if filename:
        file_path: str = os.path.join(path, filename) if path else filename
        create_file(file_path)


if __name__ == "__main__":
    main()