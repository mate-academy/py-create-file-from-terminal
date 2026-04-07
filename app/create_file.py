import sys
import os
from datetime import datetime
from typing import List, Optional, Tuple


def parse_args() -> Tuple[List[str], Optional[str]]:
    folders = []
    filename = None
    for i, arg in enumerate(sys.argv):
        if arg == "-d":
            for folder in sys.argv[i + 1:]:
                if folder.startswith("-f"):
                    break
                folders.append(folder)
        if arg == "-f":
            filename = sys.argv[i + 1]
    return folders, filename


def create_dirs(folders: List[str]) -> Optional[str]:
    if folders:
        path = os.path.join(*folders)
        os.makedirs(path, exist_ok=True)
        return path
    return None


def write_content(filepath: str) -> None:
    lines: List[str] = []
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        lines.append(content)

    if not lines:
        return

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath, "a") as file:
            file.write("\n")

    with open(filepath, "a") as file:
        file.write(f"{timestamp}\n")
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")


def main() -> None:
    folders, filename = parse_args()
    path = create_dirs(folders)

    if filename:
        if path:
            filepath = os.path.join(path, filename)
        else:
            filepath = filename
        write_content(filepath)


if __name__ == "__main__":
    main()
