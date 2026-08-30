import os
import sys
from datetime import datetime

args = sys.argv[1:]
dirs = []
filename = None
parsing_mode = None

for arg in args:
    if arg == "-d":
        parsing_mode = "d"
    elif arg == "-f":
        parsing_mode = "f"
    else:
        if parsing_mode == "d":
            dirs.append(arg)
        elif parsing_mode == "f" and filename is None:
            filename = arg

dir_path = ""
if dirs:
    dir_path = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)

if filename:
    file_path = os.path.join(dir_path, filename) if dir_path else filename

    is_existing = os.path.exists(file_path)

    lines = []
    while True:
        try:
            line = input("Enter content line: ")
        except EOFError:
            break

        if line == "stop":
            break
        lines.append(line)

    with open(file_path, "a", encoding="utf-8") as f:
        if is_existing:
            f.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(timestamp + "\n")
        for i, content in enumerate(lines, 1):
            f.write(f"{i} {content}\n")
