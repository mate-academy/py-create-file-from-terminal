import sys
import os
from datetime import datetime
from typing import List, Optional


args = sys.argv[1:]

dirs: List[str] = []
filename: Optional[str] = None


def print_usage() -> None:
    print("Usage:")
    print("  python create_file.py -f filename")
    print("  python create_file.py -d dir1 dir2")
    print("  python create_file.py -d dir1 dir2 -f filename")
    print("Then enter lines of content. Type 'stop' to finish.\n")
    sys.exit(1)


if not args:
    print("❌ No arguments provided.")
    print_usage()

if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 >= len(args) or args[f_index + 1].startswith("-"):
        print("Missing file name after '-f'.")
        print_usage()
    filename = args[f_index + 1]

if "-f" not in args and "-d" not in args:
    print("You must provide at least '-f' or '-d'.")
    print_usage()

if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        dirs = args[d_index + 1:f_index]
    else:
        dirs = args[d_index + 1:]

dir_path = os.path.join(*dirs) if dirs else "."
if dirs:
    os.makedirs(dir_path, exist_ok=True)

if filename is not None:
    assert isinstance(filename, str)
    filepath = os.path.join(dir_path, filename)
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            old_content = f.read()
        content = old_content + "\n\n" + now + "\n"
    else:
        content = now + "\n"

    for i, line in enumerate(lines, 1):
        content += f"{i} {line}\n"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
