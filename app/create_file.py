import sys
import os
from datetime import datetime
from typing import List, Tuple


def parse_arguments(args: List[str]) -> Tuple[List[str], str]:
    dirs = []
    filename = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    return dirs, filename


def get_content_lines() -> List[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def create_file() -> None:
    args = sys.argv[1:]
    dirs, filename = parse_arguments(args)

    base_path = os.getcwd()

    if dirs:
        base_path = os.path.join(base_path, *dirs)
        os.makedirs(base_path, exist_ok=True)

    if not filename:
        return

    file_path = os.path.join(base_path, filename)
    lines = get_content_lines()

    if not lines:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            file.write("\n")  # ← ВИПРАВЛЕНО: лише один перенос рядка

        file.write(timestamp + "\n")
        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")


if __name__ == "__main__":
    create_file()
