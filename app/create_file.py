import os
import sys
from datetime import datetime

args = sys.argv[1:]
has_d = "-d" in args
has_f = "-f" in args

if has_f:
    file_name = args[args.index("-f") + 1]

if has_d:
    dirs = []

    for item in args[args.index("-d") + 1:]:
        if item == "-f":
            break
        dirs.append(item)

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

if has_d and has_f:
    full_path = os.path.join(path, file_name)
elif has_f:
    full_path = file_name
else:
    full_path = None

if full_path:
    with open(full_path, "a") as f:
        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        numbered_lines = "\n".join(
            f"{i}. {line}" for i, line in enumerate(lines, start=1)
        )

        f.write(numbered_lines + "\n")
