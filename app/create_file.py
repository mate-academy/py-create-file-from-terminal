import sys
import os
import datetime


arg = sys.argv
path_dir = None
file_name = None

if "-d" in arg:
    d_index = arg.index("-d")
    dir_parts = []
    for item in arg[d_index + 1:]:
        if item.startswith("-"):
            break
        dir_parts.append(item)
    path_dir = os.path.join(*dir_parts)
    os.makedirs(path_dir, exist_ok=True)

if "-f" in arg:
    f_index = arg.index("-f")
    file_name = arg[f_index + 1]

if file_name:
    if path_dir:
        full_path = os.path.join(path_dir, file_name)
    else:
        full_path = file_name
    text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    count = 1
    while True:
        new_line = input("Enter content line: ")
        if new_line == "stop":
            break
        text += f"{count} {new_line}\n"
        count += 1

    with open(full_path, "a") as fp:
        fp.write(text)
