import os
import sys
from datetime import datetime

args = sys.argv[1:]
dir_path = []
file_name = None

if "-d" in args:
    d_idx = args.index("-d")
    for i in range(d_idx + 1, len(args)):
        if args[i] == "-f":
            break
        dir_path.append(args[i])

if "-f" in args:
    f_idx = args.index("-f")
    if f_idx + 1 < len(args):
        file_name = args[f_idx + 1]

full_path = os.path.join(*dir_path) if dir_path else ""
if full_path:
    os.makedirs(full_path, exist_ok=True)

if file_name:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    file_path = os.path.join(full_path, file_name)
    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as f:
        if file_exists:
            f.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")

        for index, line in enumerate(content_lines, start=1):
            f.write(f"{index} {line}\n")
