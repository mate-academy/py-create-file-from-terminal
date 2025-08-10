import sys
import os
from datetime import datetime

args = sys.argv[1:]

dir_path = ""
if "-d" in args:
    d_index = args.index("-d")
    dir_path_parts = []
    for item in args[d_index + 1:]:
        if item.startswith("-"):
            break
        dir_path_parts.append(item)
    dir_path = os.path.join(*dir_path_parts)
    os.makedirs(dir_path, exist_ok=True)
    print("Directory created:", dir_path)

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"\n{now}\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")

    print("File saved to:", file_path)
