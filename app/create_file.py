import os
import sys
from datetime import datetime


def get_dirs(args: list) -> list:
    if "-d" not in args:
        return []
    d_index = args.index("-d")
    list_of_dirs = []
    for arg in args[d_index + 1:]:
        if arg.startswith("-"):
            break
        list_of_dirs.append(arg)
    return list_of_dirs


def get_filename(args: list) -> str | None:
    if "-f" not in args:
        return None
    f_index = args.index("-f")
    return args[f_index + 1]


def write_content_in_file(filepath: str) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    existing_file = os.path.exists(filepath) and os.path.getsize(filepath) > 0
    with open(filepath, "a") as f:
        if existing_file:
            f.write("\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp + "\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    dirs = get_dirs(args)
    filename = get_filename(args)
    if dirs and not filename:
        dirs_path = os.path.join(*dirs)
        os.makedirs(dirs_path, exist_ok=True)
        print(f"Creating new directory: {dirs_path}")
        return
    if filename and not dirs:
        filepath = filename
        write_content_in_file(filepath)
        print(f"Writing filename: {filename}")
        return
    if dirs and filename:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
        filepath = os.path.join(dir_path, filename)
        write_content_in_file(filepath)
        print(f"Creating directory and writing filename: {filepath}")
        return


main()
