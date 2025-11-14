import sys
import os
from datetime import datetime
from typing import List


def read_content() -> List[str]:
    lines: List[str] = []
    while True:
        line: str = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_content(filepath: str, lines: List[str]) -> None:
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")
        f.write("\n")


def main() -> None:
    args: List[str] = sys.argv[1:]

    if "-d" in args:
        d_index: int = args.index("-d")
        dirs: List[str] = []
        i: int = d_index + 1
        while i < len(args) and args[i] not in ["-f", "-d"]:
            dirs.append(args[i])
            i += 1
        dir_path: str = os.path.join(*dirs) if dirs else ""
    else:
        dir_path = ""

    if "-f" in args:
        f_index: int = args.index("-f")
        filename: str = args[f_index + 1]
    else:
        print("Error: file name is required with -f flag.")
        return

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
        filepath: str = os.path.join(dir_path, filename)
    else:
        filepath = filename

    lines: List[str] = read_content()
    write_content(filepath, lines)
