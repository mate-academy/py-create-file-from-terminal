import sys
import os
from datetime import datetime

args = sys.argv[1:]

if not args:
    print("No arguments provided.")
    sys.exit(1)

directory_path = ""
file_name = None

if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        dirs = args[d_index + 1:f_index]
    else:
        dirs = args[d_index + 1:]
    if dirs:
        directory_path = os.path.join(*dirs)
        os.makedirs(directory_path, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 >= len(args):
        print("File name not provided.")
        sys.exit(1)
    file_name = args[f_index + 1]

if not file_name:
    sys.exit(0)

lines = []

while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)

if not lines:
    sys.exit(0)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

numbered_lines = []
for i, line in enumerate(lines, start=1):
    numbered_lines.append(f"{i} {line}")

block = timestamp + "\n" + "\n".join(numbered_lines) + "\n"

if directory_path:
    full_path = os.path.join(directory_path, file_name)
else:
    full_path = file_name

file_exists = os.path.exists(full_path)

mode = "a" if file_exists else "w"

with open(full_path, mode, encoding="utf-8") as f:
    if file_exists:
        f.write("\n")
    f.write(block)