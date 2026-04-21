import os
import sys
from datetime import datetime


args = sys.argv

dir_names = []
file_names = []

if "-d" in args:
    d_index = args.index("-d")
    dir_names.append(args[d_index + 1])
    dir_names.append(args[d_index + 2])

if "-f" in args:
    f_index = args.index("-f")
    file_names = args[f_index + 1]

path = ""
if dir_names:
    path = os.path.join(*dir_names)
    os.makedirs(path, exist_ok=True)

if dir_names and not file_names:
    exit()

if file_names:
    path_to_files = os.path.join(path, file_names) if path else file_names

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    date_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    for index, line in enumerate(lines):
        date_text += f"{index + 1}. {line}\n"

    mode = "a" if os.path.exists(path_to_files) else "w"

    with open(path_to_files, mode) as f:
        if mode == "w":
            f.write("\n")
        f.write(date_text)
