import sys
import os
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    if not args:
        return

    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
            continue
        if args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
            continue
        i += 1

    directory_path = ""
    if dir_parts:
        directory_path = os.path.join(*dir_parts)
        os.makedirs(directory_path, exist_ok=True)

    if not file_name:
        return

    full_path = file_name
    if directory_path:
        full_path = os.path.join(directory_path, file_name)

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mode = "a" if os.path.exists(full_path) else "w"
    with open(full_path, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n")
        f.write(f"{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            f.write(f"{idx} {line}\n")


if __name__ == "__main__":
    main()
