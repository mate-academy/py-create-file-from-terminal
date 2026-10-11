import sys
import os
from datetime import datetime

args = sys.argv[1:]
dirs = []
file_name = ""

if "-d" in args:
    d_idx = args.index("-d")
    f_idx = args.index("-f") if "-f" in args else len(args)

    if d_idx < f_idx:
        dirs = args[d_idx + 1:f_idx]
    else:
        dirs = args[d_idx + 1:]

if "-f" in args:
    f_idx = args.index("-f")
    file_name = args[f_idx + 1]

if dirs:
    os.makedirs(os.path.join(*dirs), exist_ok=True)

if file_name:
    path = os.path.join(*dirs, file_name) if dirs else file_name

    # Check if the file exists and is not empty to add a separator
    add_newline = os.path.exists(path) and os.path.getsize(path) > 0

    with open(path, "a") as file:
        if add_newline:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_num} {line}\n")
            line_num += 1
