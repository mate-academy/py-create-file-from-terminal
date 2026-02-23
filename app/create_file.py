import os
import sys
from datetime import datetime

args = sys.argv[1:]
has_d = "-d" in args
has_f = "-f" in args

file_name = None
path = None
full_path = None

if has_f:
    f_index = args.index("-f")
    if f_index + 1 >= len(args):
        print("Error: -f flag requires a filename.")
        sys.exit(1)
    file_name = args[f_index + 1]

if has_d:
    d_index = args.index("-d")
    dirs = []

    for item in args[d_index + 1:]:
        if item == "-f":
            break
        dirs.append(item)

    if not dirs:
        print("Error: -d flag requires at least one directory name.")
        sys.exit(1)

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    print("Created directory:", path)

if has_d and not has_f:
    sys.exit(0)

if path and file_name:
    full_path = os.path.join(path, file_name)
elif file_name:
    full_path = file_name

if not full_path:
    print("Error: No file specified. Use -f to specify a file.")
    sys.exit(1)

lines = []
while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

file_exists = os.path.exists(full_path)

with open(full_path, "a+") as file:
    if file_exists and os.path.getsize(full_path) > 0:
        file.write("\n")

    file.write(timestamp + "\n")

    numbered_lines = "\n".join(
        f"{i}. {line}" for i, line in enumerate(lines, start=1)
    )

    file.write(numbered_lines + "\n")

print("Written to", full_path)
