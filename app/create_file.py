import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    if not args:
        print("Usage:")
        print("  python create_file.py -d dir1 dir2 ...")
        print("  python create_file.py -f filename")
        print("  python create_file.py -d dir1 dir2 ... -f filename")
        return

    dir_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        for i in range(d_index + 1, len(args)):
            if args[i] == "-f":
                break
            dir_parts.append(args[i])

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            print("Error: -f flag requires a file name")
            return

    base_path = os.getcwd()
    if dir_parts:
        dir_path = os.path.join(base_path, *dir_parts)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = base_path

    if file_name is None:
        print(f"Directory created at: {dir_path}")
        return

    file_path = os.path.join(dir_path, file_name)

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = [timestamp]
    for i, line in enumerate(lines, start=1):
        content.append(f"{i} {line}")

    with open(file_path, "a", encoding="utf-8") as f:
        f.write("\n".join(content) + "\n\n")

    print(f"File created/updated at: {file_path}")
