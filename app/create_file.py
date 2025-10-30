import os
import sys
import datetime


args = sys.argv[1:]
if "-d" in args:
    d_index = args.index("-d")
else:
    d_index = -1

if "-f" in args:
    f_index = args.index("-f")
else:
    f_index = -1

dirs = []
if d_index != -1:
    if f_index != -1:
        dirs = args[d_index + 1: f_index]
    else:
        dirs = args[d_index + 1:]
dir_path = os.path.join(*dirs) if dirs else ""

if dir_path:
    os.makedirs(dir_path, exist_ok=True)

if f_index != -1:
    file_name = args[f_index + 1]
    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(file_path):
        content = f"\n{timestamp}\n"
    else:
        content = f"{timestamp}\n"

    for line_number, line in enumerate(lines, start=1):
        content += f"{line_number} {line} \n"

    with open(file_path, "a", encoding="utf-8") as output_file:
        output_file.write(content)
