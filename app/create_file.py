import sys
import os
from datetime import datetime

args = sys.argv[1:]
dirs = []
file_name = None
mode = None

for arg in args:
    if arg == "-d":
        mode = "d"
    elif arg == "-f":
        mode = "f"
    else:
        if mode == "d":
            dirs.append(arg)
        elif mode == "f" and file_name is None:
            file_name = arg

dir_path = ""
if dirs:
    dir_path = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)

if file_name:
    if dir_path:
        file_path = os.path.join(dir_path, file_name)
    else:
        file_path = file_name

    lines = []
    while True:
        try:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)
        except EOFError:
            break

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    add_empty_line = (os.path.exists(file_path)
                      and os.path.getsize(file_path) > 0)

    with open(file_path, "a") as f:
        if add_empty_line:
            f.write("\n")
        f.write(timestamp + "\n")
        for i, line in enumerate(lines, 1):
            f.write(f"{i} {line}\n")
