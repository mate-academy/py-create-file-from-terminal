import sys
import os
from datetime import datetime

args = sys.argv[1:]
dir_path = ""
file_name = ""
content_lines = []

if "-d" in args:
    d_index = args.index("-d")
    try:
        next_flag = args.index("-d", d_index + 1)
        dir_parts = args[d_index + 1: next_flag]
    except ValueError:
        dir_parts = args[d_index + 1:]
        dir_path = os.path.join(*dir_parts)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

        full_path = os.path.join(dir_path, file_name) \
            if dir_path else file_name

        print("Enter content line:")
        while True:
            line = input()
            if line.lower() == "stop":
                break
            content_lines.append(line)

        with open(full_path, "a", encoding="utf-8") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n{timestamp}\n")
            for i, line in enumerate(content_lines, start=1):
                f.write(f"{i} {line}\n")
