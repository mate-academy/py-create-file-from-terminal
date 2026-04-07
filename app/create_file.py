import sys
import os
from datetime import datetime

folders = []
filename = None

for i, arg in enumerate(sys.argv):
    if arg == "-d":
        for folder in sys.argv[i + 1:]:
            if folder.startswith("-f"):
                break
            folders.append(folder)
    if arg == "-f":
        filename = sys.argv[i + 1]

if folders:
    path = os.path.join(*folders)
    os.makedirs(path, exist_ok=True)
    if filename:
        filename = os.path.join(path, filename)

lines = []
while True:
    content = input("Enter content line: ")
    if content == "stop":
        break
    lines.append(content)

if lines:
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"{timestamp}\n")
        for i, line in enumerate(lines, 1):
            file.write(f"{i} {line}\n")
        file.write("\n")
