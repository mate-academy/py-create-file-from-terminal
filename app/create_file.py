import os
import sys
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

if filename:
    filepath = os.path.join(path, filename)

    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(filepath) and os.path.getsize(filepath) > 0

    with open(filepath, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(f"{now}\n")
        for index, line in enumerate(content_lines, start=1):
            f.write(f"{index} {line}\n")
