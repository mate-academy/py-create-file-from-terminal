import os
import sys
from datetime import datetime
from typing import List


def create_file() -> None:
    args: List[str] = sys.argv[1:]
    dir_path_parts: List[str] = []
    file_name: str = ""
    index: int = 0
    while index < len(args):
        if args[index] == "-d":
            index += 1
            while index < len(args) and not args[index].startswith("-"):
                dir_path_parts.append(args[index])
                index += 1
            continue
        if args[index] == "-f":
            if index + 1 < len(args):
                file_name = args[index + 1]
                index += 2
            continue
        index += 1
    full_dir_path: str = ""
    if dir_path_parts:
        full_dir_path = os.path.join(*dir_path_parts)
        os.makedirs(full_dir_path, exist_ok=True)
    if not file_name:
        return
    full_file_path: str = os.path.join(full_dir_path, file_name)
    content_lines: List[str] = []
    while True:
        line: str = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(full_file_path, "a") as target_file:
        target_file.write(f"{timestamp}\n")
        for line_idx, line_text in enumerate(content_lines, start=1):
            target_file.write(f"{line_idx} {line_text}\n")
        target_file.write("\n")


if __name__ == "__main__":
    create_file()
