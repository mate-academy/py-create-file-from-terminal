import sys
import os
from datetime import datetime


n = sys.argv
dirs = []
file_name = None
mode = None

for arg in n[1:]:
    if arg == "-d":
        mode = "dir"
    elif arg == "-f":
        mode = "file"
    else:
        if mode == "dir":
            dirs.append(arg)
        elif mode == "file":
            file_name = arg

dir_path = ""
if len(dirs) > 0:
    dir_path = os.path.join(*dirs)
if dir_path:
    os.makedirs(dir_path, exist_ok=True)

if file_name:
    final_path = os.path.join(dir_path, file_name)

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(final_path) and os.path.getsize(final_path) > 0

    with open(final_path, "a") as f:
        if file_exists:
            f.write("\n")
        f.write(current_time + "\n")

        for index, content in enumerate(lines, start=1):
            f.write(f"{index} {content}\n")
