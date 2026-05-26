import sys
import os
from datetime import datetime


args = sys.argv[1:]
dirs = []

if "-d" in args:
    for folder in args[args.index("-d") + 1:]:
        if folder == "-f":
            break
        dirs.append(folder)
    if dirs:
        os.makedirs(os.path.join(*dirs), exist_ok=True)


file_name = None
if "-f" in args:
    file_name = args[args.index("-f") + 1]

if file_name:
    if dirs:
        path = os.path.join(*dirs, file_name)
    else:
        path = file_name

    lines = []
    line = input("Enter content line: ")
    while line != "stop":
        lines.append(line)
        line = input("Enter content line: ")

    if os.path.exists(path):
        files = open(path, "a")
        files.write("\n")
    else:
        files = open(path, "w")

    files.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    for i, content in enumerate(lines, 1):
        files.write(f"{i} {content}\n")
    files.close()
