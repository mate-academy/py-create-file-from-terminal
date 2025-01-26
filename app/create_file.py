import sys
import os
from datetime import datetime


directory = sys.argv[1:]
flags = ["-d", "-f"]
directory_path = ""
file_name = ""
for i in directory:
    if i not in flags:
        directory_path += f"{i} "
if "-f" in directory:
    f_index = directory.index("-f") + 1
    if f_index < len(directory):
        file_name = directory[f_index]
path = "/".join(directory_path.split())
dir_path = os.path.dirname(path)
if dir_path:
    os.makedirs(dir_path, exist_ok=True)

with open(path, "a") as data:
    data.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    line_count = 1
    while True:
        content_line = input("Enter content line:")
        if content_line.lower() == "stop":
            data.write("\n")
            break
        data.write(f"{line_count} {content_line}\n")
        line_count += 1
