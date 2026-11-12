import os
import sys
from datetime import datetime

args = sys.argv[1:]

dirs = []
filename = None

if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        if d_index < f_index:
            dirs = args[d_index + 1 : f_index]
        else:
            dirs = args[d_index + 1 :]
    else:
        dirs = args[d_index + 1 :]

if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 < len(args):
        filename = args[f_index + 1]

dir_path = ""
if dirs:
    dir_path = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)

if filename:
    file_path = os.path.join(dir_path, filename) if dir_path else filename

    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        lines.append(user_input)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            file.write(f"{idx} {line}\n")
