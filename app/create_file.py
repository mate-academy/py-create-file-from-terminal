import sys
import os
from datetime import datetime

args = sys.argv[1:]

dirs = []
file_name = None

i = 0
while i < len(args):
    if args[i] == "-d":
        i += 1
        while i < len(args) and not args[i].startswith("-"):
            dirs.append(args[i])
            i += 1
        continue

    if args[i] == "-f":
        if i + 1 < len(args):
            file_name = args[i + 1]
            i += 2
        else:
            i += 1
        continue

    i += 1

path = ""
if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

if file_name:
    full_path = os.path.join(path, file_name) if path else file_name

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content_block = timestamp

    for idx, line in enumerate(lines, 1):
        content_block += f"\n{idx} {line}"

    if os.path.exists(full_path):
        with open(full_path, "a", encoding="utf-8") as f:
            f.write(content_block)
    else:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write("\n" + content_block)

    print(f"{full_path} created/updated")
else:
    if path:
        print(f"Directory {path} created")
    else:
        print("Nothing to do (no -d or -f provided)")
