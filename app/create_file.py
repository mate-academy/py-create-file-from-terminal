import os
import sys
from datetime import datetime


arguments = sys.argv[1:]
directories = []
file_name = None
directory_path = None


if "-f" in arguments:
    f_index = arguments.index("-f")
    file_name = arguments[f_index + 1]

if "-d" in arguments:
    d_index = arguments.index("-d")
    if "-f" in arguments and f_index > d_index:
        dir_args = arguments[d_index + 1 : f_index]
    else:
        dir_args = arguments[d_index + 1 :]
    if dir_args:
        directory_path = os.path.join(*dir_args)

if directory_path:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

if file_name:
    if directory_path:
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = file_name

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(file_path)
    with open(file_path, "a") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for index, line in enumerate(lines, 1):
            file.write(f"{index} {line}\n")
