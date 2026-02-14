import sys
import os
from datetime import datetime

args = sys.argv
path = []

if "-d" in args:
    position = args.index("-d")
    for arg in args[position + 1:]:
        if arg != "-f":
            path.append(arg)
        else:
            break

    caminho = os.path.join(*path)
    os.makedirs(caminho, exist_ok=True)

if "-f" in args:
    i = args.index("-f")
    archive_name = args[i + 1]
    if path:
         archive_name = os.path.join(caminho, archive_name)
    lines = []
    while True:
        line = input("Enter content line:")
        if line == "stop":
            break
        lines.append(line)
    if os.path.exists(archive_name):
        with open(archive_name, "a") as archive:
            archive.write("\n")
    with open(archive_name, "a") as archive:
        archive.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for i, line in enumerate(lines, start=1):
            archive.write(f"{i} {line}\n")
