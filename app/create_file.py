import sys
import os
from datetime import datetime

args = sys.argv[1:]

if not args:
    print("No arguments provided.")
    sys.exit(1)

directory_path = ""
file_name = None
dirs = []

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
            file_name = args[i]
        else:
            print("File name not provided.")
            sys.exit(1)
    else:
        i += 1

if dirs:
    directory_path = os.path.join(*dirs)
    os.makedirs(directory_path, exist_ok=True)

if not file_name:
    print("File name not provided.")
    sys.exit(1)

lines = []
while True:
    line = input("Enter content line: ").strip()
    if line.lower() == "stop":
        break
    if line:
        lines.append(line)

if not lines:
    sys.exit(0)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

numbered_lines = [f"{i} {line}" for i, line in enumerate(lines, start=1)]
block = timestamp + "\n" + "\n".join(numbered_lines) + "\n"

full_path = os.path.join(directory_path,
                         file_name) if directory_path else file_name
file_exists = os.path.exists(full_path)
mode = "a" if file_exists else "w"

with open(full_path, mode, encoding="utf-8") as output_file:
    if file_exists:
        output_file.write("\n")
    output_file.write(block)

print(f"Content written to {full_path}")
