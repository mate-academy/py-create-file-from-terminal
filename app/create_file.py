import sys
import os
from datetime import datetime

file_name = None
dirs = []
args = sys.argv

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

if "-d" in args:
    d_index = args.index("-d")
    # Якщо -f є і він стоїть ПІСЛЯ -d
    if "-f" in args and args.index("-f") > d_index:
        dirs = args[d_index + 1: args.index("-f")]
    else:
        dirs = args[d_index + 1:]

if dirs:
    dir_path = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)

if file_name:
    if dirs:
        full_file_path = os.path.join(dir_path, file_name)
    else:
        full_file_path = file_name

    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    with open(full_file_path, "a") as f:
        if (os.path.exists(full_file_path)
                and os.path.getsize(full_file_path) > 0):
            f.write("\n")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{current_time}\n")

        line_number = 1
        for text in content_lines:
            f.write(f"{line_number} {text}\n")
            line_number += 1
