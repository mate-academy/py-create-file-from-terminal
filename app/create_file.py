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
    if path:
        dir_path = os.path.join(*path)
        os.makedirs(dir_path, exist_ok=True)
    else:
        print("Error: -d flag requires at least one directory name")
        sys.exit(1)

if "-f" in args and len(args) > 2:
    i = args.index("-f")
    if i + 1 >= len(args):  # ← Verificar se existe próximo argumento
        print("Error: -f flag requires a filename")
        sys.exit(1)
    archive_name = args[i + 1]
    if path:
        archive_name = os.path.join(dir_path, archive_name)
    lines = []
    while True:
        line = input("Enter content line: ")
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
