import os
import sys
from datetime import datetime


def parse_args(args: list) -> tuple:
    filename = None
    dirs = []

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]

    if "-d" in args:
        d_index = args.index("-d")
        for arg in args[d_index + 1 :]:
            if arg == "-f":
                break
            dirs.append(arg)

    return filename, dirs


def collect_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_content(path: str, filename: str, content_lines: list) -> None:
    full_path = os.path.join(path, filename)

    old_content = ""
    if os.path.exists(full_path):
        with open(full_path, "r") as f:
            old_content = f.read()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_lines = [timestamp]
    for i, line in enumerate(content_lines, start=1):
        new_lines.append(f"{i} {line}")

    new_block = "\n".join(new_lines) + "\n"

    with open(full_path, "w") as f:
        if old_content:
            f.write(old_content.rstrip("\n") + "\n\n")
        f.write(new_block)


arguments = sys.argv[1:]
file_to_create, directories = parse_args(arguments)

target_path = os.path.join(*directories) if directories else ""
if target_path:
    os.makedirs(target_path, exist_ok=True)

if file_to_create:
    user_content = collect_content()
    write_content(target_path, file_to_create, user_content)
