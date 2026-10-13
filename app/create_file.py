import os
import sys
from datetime import datetime

dirs = []
file_name = None
current_flag = None

for arg in sys.argv[1:]:
    if arg == "-d":
        current_flag = "-d"
    elif arg == "-f":
        current_flag = "-f"
    else:
        if current_flag == "-d":
            dirs.append(arg)
        elif current_flag == "-f":
            file_name = arg
            current_flag = None

path = ""
if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

if file_name:
    file_path = os.path.join(path, file_name) if path else file_name

    add_empty_line =\
        os.path.exists(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a") as f:
        if add_empty_line:
            f.write("\n")

        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{line_count} {line}\n")
            line_count += 1
