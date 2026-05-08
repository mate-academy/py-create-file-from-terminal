import os
import sys
from datetime import datetime


args = sys.argv[1:]

directory = None
file_name = None

if "-d" in args:
    d_idx = args.index("-d")
    path_parts = []
    for i in range(d_idx + 1, len(args)):
        if args[i].startswith("-"):
            break
        path_parts.append(args[i])

    if path_parts:
        directory = os.path.join(*path_parts)

if "-f" in args:
    f_idx = args.index("-f")
    if f_idx + 1 < len(args):
        file_name = args[f_idx + 1]

if directory:
    os.makedirs(directory, exist_ok=True)

if directory and file_name:
    path = os.path.join(directory, file_name)
elif file_name:
    path = file_name

if file_name:
    with open(path, "a") as archive:
        if os.path.exists(path) and os.path.getsize(path) > 0:
            archive.write("\n")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archive.write(f"{current_time}\n")

        count = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            archive.write(f"{count} {line}\n")
            count += 1
