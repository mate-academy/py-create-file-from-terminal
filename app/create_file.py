import sys
import os
from datetime import datetime

args = sys.argv[1:]

dirs = []
filename = None
current_flag = None
for arg in args:
    if arg == "-d":
        current_flag = "-d"
    elif arg == "-f":
        current_flag = "-f"
    else:
        if current_flag == "-d":
            dirs.append(arg)
        elif current_flag == "-f" and filename is None:
            filename = arg

dir_path = ""

if dirs:
    dir_path = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)

if filename:
    file_path = os.path.join(dir_path, filename) if dir_path else filename
    file_exists = (
        os.path.exists(file_path) and os.path.getsize(file_path)
    )

    lines = []
    while True:
        try:
            line = input("Enter content line: ")
        except EOFError:
            break

        if line == "stop":
            break

        lines.append(line)

    if lines:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, "a") as f:
            if file_exists:
                f.write("\n")

            f.write(f"{timestamp}\n")
            for i, line in enumerate(lines, 1):
                f.write(f"{i} {line}\n")
