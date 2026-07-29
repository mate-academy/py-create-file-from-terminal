import os
import sys
from datetime import datetime


args = sys.argv[1:]

directories = []
filename = None

if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")
        directories = args[d_index + 1:f_index]
    else:
        directories = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")

    if f_index + 1 < len(args):
        filename = args[f_index + 1]

path = os.path.join(*directories) if directories else ""

if path:
    os.makedirs(path, exist_ok=True)

if filename is None:
    sys.exit()

file_path = os.path.join(path, filename)

lines = []

while True:
    line = input("Enter content line: ")

    if line == "stop":
        break

    lines.append(line)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

mode = "a" if os.path.exists(file_path) else "w"

with open(file_path, mode, encoding="utf-8") as file:
    if mode == "a":
        file.write("\n\n")

    file.write(f"{timestamp}\n")

    for number, line in enumerate(lines, start=1):
        file.write(f"{number} {line}\n")
