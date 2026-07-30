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

        if d_index < f_index:
            directories = args[d_index + 1:f_index]
        else:
            directories = args[d_index + 1:]
    else:
        directories = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")

    if f_index + 1 < len(args):
        filename = args[f_index + 1]

path = os.path.join(*directories) if directories else ""

if path:
    os.makedirs(path, exist_ok=True)

if filename:
    file_path = os.path.join(path, filename)

    content = []
    line_number = 1

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content.append(f"{line_number} {line}")
        line_number += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode, encoding="utf-8") as file:
        if mode == "a":
            file.write("\n")

        file.write(f"{timestamp}\n")
        file.write("\n".join(content))
        file.write("\n")
