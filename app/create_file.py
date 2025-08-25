import sys
import os
from datetime import datetime
from typing import List

args: List[str] = sys.argv[1:]
dir_path: str = ""
file_name: str = ""
content_lines: List[str] = []

if "-d" in args:
    d_index: int = args.index("-d")
    try:
        next_flag: int = args.index("-f", d_index + 1)
        dir_parts: List[str] = args[d_index + 1: next_flag]
    except ValueError:
        dir_parts = args[d_index + 1:]
    dir_path = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)

if "-f" in args:
    f_index: int = args.index("-f")
    file_name = args[f_index + 1]

    full_path: str = os.path.join(dir_path, file_name) \
        if dir_path else file_name

    while True:
        line: str = input("Enter content line: ")
        if line == "stop":   # case-sensitive
            break
        content_lines.append(line)

    if content_lines:
        mode: str = "a" if os.path.exists(full_path) else "w"
        with open(full_path, mode, encoding="utf-8") as f:
            if os.path.getsize(full_path) > 0:
                f.write("\n")

            timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp}\n")
            for i, line in enumerate(content_lines, start=1):
                f.write(f"{i} {line}\n")
