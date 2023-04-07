import sys
import os
from datetime import datetime

args = sys.argv[1:]
dir_path = ""
file_name = ""
file_content = ""

if "dir" in args:
    idx = args.index("dir")
    dir_path = os.path.join(*args[idx + 1:])
    os.makedirs(dir_path, exist_ok=True)

if "file" in args:
    idx = args.index("file")
    file_name = args[idx + 1]
    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [f"{i} {line}" for i, line in enumerate(lines, start=1)]
    content = f"{timestamp}\n" + "\n".join(lines) + "\n"

    mode = "a" if os.path.isfile(file_path) else "w"
    with open(file_path, mode) as f:
        f.write(content)
