import sys
import os
from datetime import datetime


args = sys.argv[1:]

directories = []
file_name = None

if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        directories = args[d_index + 1: f_index]
    else:
        directories = args[d_index + 1:]

if directories:
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    if directories:
        file_name = os.path.join(dir_path, file_name)
    with open(file_name, "a") as file:
        time_stamp = datetime.now()
        file.write(time_stamp.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for index, line in enumerate(lines, 1):
            file.write(f"{index} {line}\n")
        file.write("\n")
