import os
import sys

from datetime import datetime


directory_path = "."
file_name = "file.txt"

args = sys.argv

for i in range(len(args)):
    if args[i] == "-d":
        j_arg = i + 1

        parts = []
        while j_arg < len(args) and not args[i].startswith("-"):
            parts.append(args[j_arg])
            j_arg += 1

        if parts:
            directory_path = os.path.join(*parts)

    if args[i] == "-f":
        file_name = args[i + 1]

if directory_path:
    os.makedirs(directory_path, exist_ok=True)

full_path = os.path.join(str(directory_path), file_name)

lines = []
while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)

with open(full_path, "a") as f:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write("\n" + current_time + "\n")

    number = 1
    for text in lines:
        f.write(f"{number} {text}\n")
        number += 1
