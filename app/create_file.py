import sys
import os
from datetime import datetime


args = sys.argv[1:]
folder = "."
file_name = None

if "-d" in args:
    i = args.index("-d")
    parts = args[i + 1:]

    dir_parts = []
    for char in parts:
        if char == "-f":
            break
        dir_parts.append(char)

    folder = os.path.join(*dir_parts)
    os.makedirs(folder, exist_ok=True)


if "-f" in args:
    i = args.index("-f")
    file_name = args[i + 1]

    file_path = os.path.join(folder, file_name)

    lines = []
    while True:
        text = input("Enter content line: ")
        if text == "stop":
            break
        lines.append(text)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    block = [timestamp]
    for i, line in enumerate(lines, 1):
        block.append(f"{i} {line}")

    text = "\n".join(block)

    if os.path.exists(file_path):
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("\n\n" + text)
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)
