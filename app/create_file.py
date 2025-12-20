import sys
import os
from datetime import datetime

arguments = sys.argv[1:]
directories, files = [], None
i = 0

while i < len(arguments):
    if arguments[i] == "-d":
        i += 1
        while i < len(arguments) and arguments[i] not in ("-d", "-f"):
            directories.append(arguments[i])
            i += 1
    elif arguments[i] == "-f":
        files = arguments[i + 1]
        i += 2

path = os.path.join(*directories) if directories else ""
if path:
    os.makedirs(path, exist_ok=True)
if not files:
    exit()

lines = []
while (file_line := input("Enter content line: ")) != "stop":
    lines.append(file_line)
if not lines:
    exit()

files_path = os.path.join(path, files) if path else files
with open(files_path, "a") as f:
    if os.path.exists(files_path) and os.path.getsize(files_path) > 0:
        f.write("\n")
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    for i, file_line in enumerate(lines, 1):
        f.write(f"{i} {file_line}\n")
