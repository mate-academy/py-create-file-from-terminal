import sys
import os
from datetime import datetime

def create_directories(dirs: list) -> str:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path

def read_input_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines

def append_to_file(path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"\n{timestamp}\n")
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")

def parse_arguments(args: list) -> list:
    dirs = []
    filename = ""
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
                print("Error: No file name provided after -f")
                sys.exit(1)
        else:
            print(f"Unknown argument: {args[i]}")
            sys.exit(1)

    return dirs, filename

def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage:\n  python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dirs, filename = parse_arguments(args)

    base_path = os.getcwd()
    if dirs:
        base_path = create_directories(dirs)

    if filename:
        file_path = os.path.join(base_path, filename)
        lines = read_input_lines()
        append_to_file(file_path, lines)
        print(f"Content written to: {file_path}")
    elif dirs:
        print(f"Directory created: {base_path}")