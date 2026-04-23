import sys
import os
from datetime import datetime

args = sys.argv

dirs = []
path = "."

if "-d" in args:
    d_index = args.index("-d") + 1

    for arg in args[d_index:]:
        if arg == "-f":
            break
        dirs.append(arg)

    if dirs:
        path = os.path.join(*dirs)
        os.makedirs(path, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f") + 1

    filename = args[f_index]
    lines = args[f_index + 1:]

    full_path = os.path.join(path, filename)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n"

    for i, line in enumerate(lines, 1):
        content += f"{i} {line}\n"

    if os.path.exists(full_path):
        content = "\n" + content

    with open(full_path, "a") as f:
        f.write(content)

    print("File created:", full_path)

elif dirs:
    print("Directories created:", path)
