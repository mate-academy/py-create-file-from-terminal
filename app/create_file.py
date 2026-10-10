import sys

import os

from datetime import datetime


args = sys.argv[1:]
directories = []
file_name = None

i = 0
while i < len(args):
    if args[i] == "-d":
        i += 1
        while i < len(args) and not args[i].startswith("-"):
            directories.append(args[i])
            i += 1
    elif args[i] == "-f":
        if i + 1 < len(args):
            file_name = args[i + 1]
        i += 2
    else:
        i += 1

path = os.path.join(*directories) if directories else "."

if directories:
    os.makedirs(path, exist_ok=True)

if file_name:
    file_path = os.path.join(path, file_name)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write("\n")

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break

            file.write(f"{line_number} {line}\n")
            line_number += 1
