import sys
import os
import datetime
from typing import List, Optional


def parse_args() -> tuple:
    args = sys.argv

    dirs = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        f_index = args.index("-f") if "-f" in args else len(args)

        dirs = args[d_index + 1:f_index]

    if "-f" in args:
        f_index = args.index("-f")

        if f_index + 1 >= len(args):
            print("Error: file name is missing")
            sys.exit(1)

        file_name = args[f_index + 1]

    return dirs, file_name


def create_directory(dirs: List[str]) -> Optional[str]:
    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)
        return path
    return None


def get_lines() -> List[str]:
    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def write_to_file(full_path: str, lines: List[str]) -> None:
    file_exists = os.path.exists(full_path) and os.path.getsize(full_path) > 0

    with open(full_path, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")


def main() -> None:
    dirs, file_name = parse_args()

    if not dirs and not file_name:
        print("Error: you must provide -d and/or -f")
        sys.exit(1)

    path = create_directory(dirs)

    if dirs and not file_name:
        return

    if file_name and not path:
        full_path = file_name

    elif file_name and path:
        full_path = os.path.join(path, file_name)

    else:
        return

    lines = get_lines()
    write_to_file(full_path, lines)


if __name__ == "__main__":
    main()
