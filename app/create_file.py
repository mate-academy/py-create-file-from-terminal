import sys
import os
from datetime import datetime

args = sys.argv[1:]

dir_path = []
file_name = None

if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 < len(args):
        file_name = args[f_index + 1]

if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args and d_index < f_index:
        dir_path = args[d_index + 1 : f_index]
    else:
        dir_path = args[d_index + 1 :]

target_dir = ""

if dir_path:
    target_dir = os.path.join(*dir_path)
    os.makedirs(target_dir, exist_ok=True)

if file_name:
    full_path = os.path.join(
        target_dir, file_name) if target_dir else file_name

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prefix = "\n" if (os.path.exists(full_path)
                      and os.path.getsize(full_path) > 0) else ""

    with open(full_path, "a") as f:
        f.write(f"{prefix}{timestamp}\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")
