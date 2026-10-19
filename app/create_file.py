import sys
import os
from datetime import datetime


d_index = sys.argv.index("-d") if "-d" in sys.argv else None
f_index = sys.argv.index("-f") if "-f" in sys.argv else None

dirs = []
if d_index is not None:
    if f_index is not None and d_index < f_index:
        dirs = sys.argv[d_index + 1:f_index]
    elif f_index is not None and d_index > f_index:
        dirs = sys.argv[d_index + 1:]
    elif f_index is None:
        dirs = sys.argv[d_index + 1:]

if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
else:
    path = ""

file_name = None
if f_index is not None and f_index + 1 < len(sys.argv):
    next_arg = sys.argv[f_index + 1]
    if not next_arg.startswith("-"):
        file_name = next_arg

if file_name:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        if line.strip() == "":
            continue
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_block = timestamp
    for index, line in enumerate(lines, start=1):
        content_block += f"\n{index} {line}"
    content_block += "\n"

    if path:
        full_file_path = os.path.join(path, file_name)
    else:
        full_file_path = file_name
    if os.path.exists(full_file_path) and os.path.getsize(full_file_path) > 0:
        content_block = "\n" + content_block

    with open(full_file_path, "a", encoding="utf-8") as f:
        f.write(content_block)

    print(f"File successfully saved: {full_file_path}")
else:
    if dirs:
        print(f"Directory(ies) successfully created: {path}")
    else:
        print("No valid flags (-d or -f) provided.")
