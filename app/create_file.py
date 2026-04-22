import sys
import os

from datetime import datetime


args = sys.argv[1:]
dirs = []
filename = None

mode = None
for arg in args:
    if arg == "-d":
        mode = "d"
    elif arg == "-f":
        mode = "f"
    else:
        if mode == "d":
            dirs.append(arg)
        elif mode == "f":
            filename = arg
            mode = None

dir_path = ""
if dirs:
    dir_path = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)

if filename:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    file_path = os.path.join(dir_path, filename) if dir_path else filename

    needs_blank_line = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a") as f:

        if needs_blank_line:
            f.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")

        for i, line_content in enumerate(lines, 1):
            f.write(f"{i} {line_content}\n")
