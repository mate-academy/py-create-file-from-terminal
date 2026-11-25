import os
import sys

from datetime import datetime


arguments = sys.argv[1:]
directories = []
file_name = None
index = 0
while index < len(arguments):
    if arguments[index] == "-d":
        index += 1
        while index < len(arguments) and not arguments[index].startswith("-"):
            directories.append(arguments[index])
            index += 1
    elif arguments[index] == "-f":
        index += 1
        if index < len(arguments):
            file_name = arguments[index]
        index += 1
    else:
        index += 1
directory_path = os.path.join(*directories) if directories else ""
if directories:
    os.makedirs(directory_path, exist_ok=True)
if file_name is not None:
    file_path = os.path.join(directory_path, file_name)
    file_exists = os.path.exists(file_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        if file_exists and os.path.getsize(file_path) > 0:
            f.write("\n")
        f.write(timestamp + "\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1
