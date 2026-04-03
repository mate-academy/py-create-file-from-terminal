import sys
import os
import datetime


if "-f" in sys.argv:
    file_index = sys.argv.index("-f") + 1
    file_name = sys.argv[file_index]
if "-d" in sys.argv:
    dir_index = sys.argv.index("-d") + 1
    if "-f" in sys.argv:
        end_index = sys.argv.index("-f")
    else:
        end_index = len(sys.argv)
folders = sys.argv[dir_index:end_index]
dir_path = os.path.join(*folders)
os.makedirs(dir_path, exist_ok=True)

if dir_path:
    full_path = os.path.join(dir_path, file_name)
else:
    full_path = file_name

with open(full_path, "a") as f:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(now + "\n")
    line_number = 1

    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        f.write(f"{line_number} {content}\n")
        line_number += 1
