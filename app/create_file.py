import os
import sys
import datetime

args = sys.argv
dirs = []
file_name = None

if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")
        dirs = args[d_index + 1:f_index]
    else:
        dirs = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

dir_path = ""

if dirs:
    dir_path = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)

if file_name:
    if dir_path:
        file_path = os.path.join(dir_path, file_name)
    else:
        file_path = file_name

    lines = []

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break

        lines.append(line)

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    content = (timestamp + "\n")
    for i, lime in enumerate(lines):
        content += f"{i} {line}\n"
    content += "\n"

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content)
