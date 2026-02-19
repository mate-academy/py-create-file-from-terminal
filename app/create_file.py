import sys
import os
from datetime import datetime

args = sys.argv[1:]

directories = []
file_name = []
checker_d = False
checker_f = False

for arg in args:
    if arg == "-d":
        checker_d = True
        checker_f = False
        continue
    if arg == "-f":
        checker_f = True
        checker_d = False
        continue
    if checker_d:
        directories.append(arg)
    if checker_f:
        file_name.append(arg)

if directories:
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)
else:
    dir_path = "."

if file_name:
    file_path = os.path.join(dir_path, file_name[0])
    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n")
        f.write(timestamp + "\n")
        for i, line in enumerate(content, start=1):
            f.write(f"{i} {line}\n")
