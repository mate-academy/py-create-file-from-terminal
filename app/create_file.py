import sys
import os
from datetime import datetime
from typing import List, Tuple, Optional


def parse_args(args: List[str]) -> Tuple[List[str], Optional[str]]:
    dirs = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                dirs.append(args[i])
                i += 1
            continue

        if args[i] == "-f":
            if i + 1 >= len(args):
                print("File name not provided after -f")
                return dirs, None
            file_name = args[i + 1]
            i += 2
            continue

        i += 1

    return dirs, file_name


def read_lines() -> List[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def write_file(path: str, file_name: str, lines: List[str]) -> None:
    file_path = os.path.join(path, file_name)

    file_exists = os.path.exists(file_path)
    mode = "a" if file_exists else "w"

    with open(file_path, mode, encoding="utf-8") as f:
        if file_exists and os.path.getsize(file_path) > 0:
            f.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp + "\n")

        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    dirs, file_name = parse_args(args)

    path = os.path.join(*dirs) if dirs else os.getcwd()

    if dirs:
        os.makedirs(path, exist_ok=True)

    if dirs and not file_name:
        return

    if not file_name:
        print("File name not provided")
        return

    lines = read_lines()

    if not lines:
        return

    write_file(path, file_name, lines)


if __name__ == "__main__":
    main()
