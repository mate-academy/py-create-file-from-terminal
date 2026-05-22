import sys
import datetime
import os

arg = sys.argv[1:]

d_idx = arg.index("-d") if "-d" in arg else -1
f_idx = arg.index("-f") if "-f" in arg else -1

dir_parts = []
filename = " "

if d_idx != -1:
    if f_idx != -1 and f_idx > d_idx:
        dir_parts = arg[d_idx + 1:f_idx]
    elif f_idx != -1 and f_idx < d_idx:
        dir_parts = arg[d_idx + 1:]
    else:
        dir_parts = arg[d_idx + 1:]

if f_idx != -1 and f_idx + 1 < len(arg):
    filename = arg[f_idx + 1]

target_dir = os.path.join(*dir_parts) if dir_parts else ""
if target_dir:
    os.makedirs(target_dir, exist_ok=True)

if f_idx != -1 and filename:
    content = []
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content.append(time_str)

    line_number = 1
    while True:
        new_line = input("Enter content line: ")
        if new_line == "stop":
            break
        content.append(f"{line_number} {new_line}")
        line_number += 1

    full_path = os.path.join(target_dir, filename) if target_dir else filename

    if os.path.exists(full_path):
        content_to_write = "\n" + "\n".join(content) + "\n"
        with open(full_path, "a") as file:
            file.write(content_to_write)
    else:
        content_to_write = "\n".join(content) + "\n"
        with open(full_path, "w") as file:
            file.write(content_to_write)
