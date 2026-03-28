import os
import sys
from datetime import datetime


def parse_args(argv: list[str]) -> tuple[list[str], str | None]:
    dir_parts = []
    file_name = None

    if "-d" in argv:
        d_index = argv.index("-d")
        for i in range(d_index + 1, len(argv)):
            if argv[i] == "-f":
                break
            dir_parts.append(argv[i])

    if "-f" in argv:
        f_index = argv.index("-f")
        if f_index + 1 < len(argv):
            file_name = argv[f_index + 1]
        else:
            print("Error: -f flag requires a file name")
            return dir_parts, None

    return dir_parts, file_name


def prompt_for_lines() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_content(filepath: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [timestamp]
    for i, line in enumerate(lines, start=1):
        content.append(f"{i} {line}")

    with open(filepath, "a", encoding="utf-8") as f:
        f.write("\n".join(content) + "\n\n")

    print(f"File created/updated at: {filepath}")


def create_file() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2 ...")
        print("  python create_file.py -f filename")
        print("  python create_file.py -d dir1 dir2 ... -f filename")
        return

    dir_parts, file_name = parse_args(args)

    if file_name is None and "-f" in args:
        return

    base_path = os.getcwd()
    dir_path = os.path.join(base_path, *dir_parts) if dir_parts else base_path
    os.makedirs(dir_path, exist_ok=True)

    if file_name is None:
        print(f"Directory created at: {dir_path}")
        return

    file_path = os.path.join(dir_path, file_name)
    lines = prompt_for_lines()
    write_content(file_path, lines)
