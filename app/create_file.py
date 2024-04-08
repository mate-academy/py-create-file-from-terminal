import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    try:
        dir_path = args[args.index("-d") + 1:args.index("-f")]
    except ValueError:
        dir_path = args[args.index("-d") + 1:] if "-d" in args else []

    try:
        file_name = args[args.index("-f") + 1]
    except (ValueError, IndexError):
        file_name = ""

    if dir_path:
        full_dir_path = os.path.join(*dir_path)
        os.makedirs(full_dir_path, exist_ok=True)
    else:
        full_dir_path = ""

    if not file_name:
        return

    full_path = os.path.join(full_dir_path, file_name) \
        if full_dir_path else file_name
    print("Enter content lines (type 'stop' to finish):")

    content_lines = []
    line = input()
    while line != "stop":
        content_lines.append(line)
        line = input()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_path, "a") as f:
        if os.path.getsize(full_path) > 0:
            f.write("\n")
        f.write(f"{timestamp}\n")
        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i}. {line}\n")


if __name__ == "__main__":
    main()
