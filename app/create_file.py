import sys
import os
from datetime import datetime


args = sys.argv[1:]
dirs = []
collect_dirs = False
for i in args:
    if i == "-d":
        collect_dirs = True
    elif i.startswith("-"):
        collect_dirs = False
    elif collect_dirs:
        dirs.append(i)

if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

filename = ""
collect_file = False
for arg in args:
    if arg == "-f":
        collect_file = True
    elif arg.startswith("-"):
        collect_file = False
    elif collect_file:
        filename = arg
        collect_file = False
if len(dirs) > 0:
    filepath = os.path.join(*dirs, filename)
else:
    filepath = filename

lines = []
while True:
    line = input("Enter new line of content: ")
    if line.lower() == "stop":
        break
    lines.append(line)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(filepath, "a", encoding="utf-8") as f:
    if os.path.exists(filepath) and os.path.getsize(filepath) > 0:
        f.write("\n\n")
    f.write(timestamp + "\n")
    for i, line in enumerate(lines, start=1):
        f.write(f"{i} {line}\n")
