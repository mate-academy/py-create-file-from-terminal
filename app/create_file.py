import sys
import os
from datetime import datetime
from typing import List, Tuple, Optional


def parse_args(args: List[str]) -> Tuple[List[str], Optional[str]]:
    dirs: List[str] = []
    file_name: Optional[str] = None

    if "-d" in args:
        d_index = args.index("-d")
        for item in args[d_index + 1:]:
            if item == "-f":
                break
            dirs.append(item)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return dirs, file_name


def create_dirs(dirs: List[str]) -> str:
    if not dirs:
        return ""

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def get_user_input() -> List[str]:
    lines: List[str] = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    return lines


def write_to_file(full_path: str, lines: List[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(full_path)

    with open(full_path, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(timestamp + "\n")

        for i, line in enumerate(lines):
            f.write(f"{i + 1} {line}\n")


def main() -> None:
    args = sys.argv[1:]

    dirs, file_name = parse_args(args)
    path = create_dirs(dirs)

    if not file_name:
        return

    full_path = os.path.join(path, file_name) if path else file_name

    lines = get_user_input()
    write_to_file(full_path, lines)


if __name__ == "__main__":
    main()
