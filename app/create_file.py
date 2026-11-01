import os
import sys
from datetime import datetime


def get_content_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_content(file_path: str) -> None:
    lines = get_content_lines()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_has_content = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a") as file:
        if file_has_content:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


def create_file() -> None:
    args = sys.argv[1:]
    directory = ""

    if "-d" in args:
        start = args.index("-d") + 1
        end = len(args)
        if "-f" in args and args.index("-f") > start:
            end = args.index("-f")
        dir_parts = args[start:end]
        if dir_parts:
            directory = os.path.join(*dir_parts)
            os.makedirs(directory, exist_ok=True)

    if "-f" in args:
        file_name = args[args.index("-f") + 1]
        write_content(os.path.join(directory, file_name))


create_file()
