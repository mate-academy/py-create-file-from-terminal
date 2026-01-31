import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def read_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    dirs = []
    filename = None
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    dir_path = os.path.join(*dirs) if dirs else ""
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)
    if filename is None:
        return

    file_path = os.path.join(dir_path, filename)
    content_lines = read_content()
    timestamp = get_timestamp()
    block_lines = [timestamp]
    for idx, line in enumerate(content_lines, start=1):
        block_lines.append(f"{idx} {line}")
    block_text = "\n".join(block_lines)
    file_exists = os.path.exists(file_path)
    with open(file_path, "a" if file_exists else "w", encoding="utf-8") as f:
        if file_exists and os.path.getsize(file_path) > 0:
            f.write("\n\n")
        f.write(block_text)


if __name__ == "__main__":
    main()
