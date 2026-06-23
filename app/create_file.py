import sys
import os

from datetime import datetime


file_way = sys.argv[1:]
dirs = []
file_name = None
if "-d" in file_way:
    start = file_way.index("-d") + 1
    for i in file_way[start:]:
        if i == "-f":
            break
        dirs.append(i)
if "-f" in file_way:
    idx = file_way.index("-f") + 1
    file_name = file_way[idx]

if dirs:
    path = "/".join(dirs)
    os.makedirs(path, exist_ok=True)

if file_name:
    path_way = os.path.join("/".join(dirs), file_name) if dirs else file_name

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path_way, "a") as f:
        if os.path.exists(path_way) and os.path.getsize(path_way) > 0:
            f.write("\n")
        f.write(f"{timestamp}\n")
        for index, line in enumerate(lines, start=1):
            f.write(f"{index} {line}\n")
