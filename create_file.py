import sys
import os
from datetime import datetime

args = sys.argv[1:]

directory_parts = []
file_name = None

"""parse arguments"""
if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")
        directory_parts = args[d_index + 1 : f_index]
    else:
        directory_parts = args[d_index + 1]

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

"""Create directory"""
path = ""

if directory_parts:
    path = os.path.join(*directory_parts)
    os.makedirs(path, exist_ok=True)

if file_name:
    if path:
        full_path = os.path.join(path, file_name)
    else:
        full_path = file_name

    """Input content"""
    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    file_exist = os.path.exists(full_path)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(full_path, "a") as file:
        file.write(timestamp + "\n")

        if file_exist and os.path.getsize(full_path) > 0:
            file.write("\n")

        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")
