from datetime import datetime
from sys import argv
import os

directories = []
filename = "file.txt"

if "-d" in argv:
    d_idx = argv.index("-d")
    for arg in argv[d_idx + 1:]:
        if arg == "-f":
            break
        directories.append(arg)

if "-f" in argv:
    f_idx = argv.index("-f")
    if f_idx + 1 < len(argv):
        filename = argv[f_idx + 1]

if directories:
    path = os.path.join(*directories)
else:
    path = ""
if path:
    os.makedirs(path, exist_ok=True)
    os.chdir(path)

file_data = [datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"]
line_count = 1

while True:
    line = input("Enter content line:")
    if line.lower() == "stop":
        break

    file_data.append(f"{line_count} {line}\n")
    line_count += 1

with open(filename, "a") as f:
    f.writelines(file_data)
