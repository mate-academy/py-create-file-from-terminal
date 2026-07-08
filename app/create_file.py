import os
import sys
from datetime import datetime

args = sys.argv[1:]

filename = None
dirs = []

if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 < len(args):
        filename = args[f_index + 1]

if "-d" in args:
    d_index = args.index("-d")
    for arg in args[d_index + 1 :]:
        if arg == "-f":
            break
        dirs.append(arg)

path = os.path.join(*dirs) if dirs else ""

if path:
    os.makedirs(path, exist_ok=True)

if filename:
    full_path = os.path.join(path, filename)

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    old_content = ""
    if os.path.exists(full_path):
        with open(full_path, "r") as f:
            old_content = f.read()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_lines = [timestamp]
    for i, line in enumerate(lines, start=1):
        new_lines.append(f"{i} {line}")

    new_block = "\n".join(new_lines) + "\n"

    with open(full_path, "w") as f:
        if old_content:
            f.write(old_content.rstrip("\n") + "\n\n")
        f.write(new_block)
