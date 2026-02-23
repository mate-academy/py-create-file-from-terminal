import os
import sys
from datetime import datetime


def build_path(parts: list) -> None:
    if not parts:
        return os.getcwd()
    return os.path.join(os.getcwd(), *parts)


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage: create_file.py [-d dir1 dir2 ...] [-f filename]")
        return
    dir_parts = []
    filename = None

    if "-d" in args:
        d_idx = args.index("-d")
        # everything after -d until -f or end
        f_idx = args.index("-f") if "-f" in args else None
        end = f_idx if f_idx is not None else len(args)
        dir_parts = args[d_idx + 1:end]

    if "-f" in args:
        f_idx = args.index("-f")
        if f_idx + 1 < len(args):
            filename = args[f_idx + 1]

        else:
            print("Error: missing filename after -f")
            return
    target_dir = create_dir(dir_parts) if dir_parts else os.getcwd()

    if filename:
        target_file = os.path.join(target_dir, filename)
        create_file(target_file)


def create_dir(dir_parts: list) -> str:
    target = build_path(dir_parts)
    os.makedirs(target, exist_ok=True)
    return target


def create_file(file_path: str) -> None:
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(timestamp + "\n")

        for i, text in enumerate(lines, start=1):
            f.write(f"{i} {text}\n")
        f.write("\n")
