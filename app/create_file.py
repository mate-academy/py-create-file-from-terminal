import os
import sys
from datetime import datetime


def parse_args() -> dict:
    args = sys.argv[1:]

    dirs = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
            continue

        if args[i] == "-f":
            i += 1
            file_name = args[i]
            i += 1
            continue

        i += 1

    return dirs, file_name


def main() -> None:
    dirs, file_name = parse_args()

    path = os.path.join(*dirs) if dirs else ""
    if path:
        os.makedirs(path, exist_ok=True)

    if not file_name:
        return

    if not file_name:
        return

    if path:
        file_path = os.path.join(str(path), file_name)
    else:
        file_path = file_name

    lines = []
    idx = 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{idx} {line}")
        idx += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    block = timestamp + "\n" + "\n".join(lines)

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            existing = f.read().strip()

        if existing:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n\n" + block)
        else:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(block)
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(block)


main()
