import os
import sys
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
    if not filename:
        print("Error: file name is required (-f)")
        return

    file_path = os.path.join(dir_path, filename)
    content_lines = read_content()
    timestamp = get_timestamp()
    output = [timestamp]
    for idx, line in enumerate(content_lines, start=1):
        output.append(f"{idx} {line}")

    text_to_write = "\n".join(output) + "\n\n"
    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode, encoding="utf-8") as f:
        f.write(text_to_write)


if __name__ == "__main__":
    main()
