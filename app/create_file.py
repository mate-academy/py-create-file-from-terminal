import os
import sys
from datetime import datetime


def parse_args(args: list) -> tuple:
    dirs = []
    filename = None
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
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


def build_path(dirs: list, filename: str | None) -> str | None:
    if dirs and filename:
        return os.path.join(*dirs, filename)
    if dirs:
        return os.path.join(*dirs)
    return filename


def read_content_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def main() -> None:
    dirs, filename = parse_args(sys.argv[1:])

    if dirs:
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)

    if filename:
        path = build_path(dirs, filename)

        lines = read_content_lines()
        numbered_lines = [
            f"{index} {line}" for index, line in enumerate(lines, start=1)
        ]

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = timestamp + "\n" + "\n".join(numbered_lines) + "\n"

        file_exists = os.path.exists(path)
        mode = "a" if file_exists else "w"

        with open(path, mode) as file:
            if file_exists:
                file.write("\n" + entry)
            else:
                file.write(entry)


main()
