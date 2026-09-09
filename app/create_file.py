import sys
import os
from datetime import datetime


dirs = []
filename = None
i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == "-d":
        i += 1
        while i < len(sys.argv) and sys.argv[i] != "-f":
            dirs.append(sys.argv[i])
            i += 1
    elif arg == "-f":
        i += 1
        if i < len(sys.argv):
            filename = sys.argv[i]
            i += 1
    else:
        i += 1

if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
else:
    path = "."

if not filename:
    print("No filename provided. Use -f <filename>")
    sys.exit(1)
file_path = os.path.join(path, filename)

lines = []
while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)
if lines:
    need_sep = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a", encoding="utf-8") as f:
        if need_sep:
            f.write("\n")
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for idx, ln in enumerate(lines, 1):
            f.write(f"{idx} {ln}\n")
