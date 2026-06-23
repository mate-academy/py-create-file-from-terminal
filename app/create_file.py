import sys
import os

from datetime import datetime


def build_directory_path(dirs: list) -> str:
    return os.path.join(*dirs)


def collect_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_block(path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(path) and os.path.getsize(path) > 0

    with open(path, "a") as output_file:
        if file_exists:
            output_file.write("\n")
        output_file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            output_file.write(f"{index} {line}\n")


args = sys.argv[1:]
dirs = []
file_name = None

if "-d" in args:
    start = args.index("-d") + 1
    for item in args[start:]:
        if item == "-f":
            break
        dirs.append(item)

if "-f" in args:
    idx = args.index("-f") + 1
    file_name = args[idx]

if dirs:
    directory_path = build_directory_path(dirs)
    os.makedirs(directory_path, exist_ok=True)

if file_name:
    path_way = os.path.join(build_directory_path(dirs),
                            file_name) if dirs else file_name
    lines = collect_lines()
    write_block(path_way, lines)
