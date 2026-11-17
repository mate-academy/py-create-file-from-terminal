import sys
import os
from datetime import datetime


arguments = sys.argv
if "-d" in arguments:
    directory_index = arguments.index("-d")
    if "-f" in arguments:
        file_index = arguments.index("-f")
        if directory_index + 1 == file_index:
            raise ValueError("Directory name is missing")
        if directory_index < file_index:
            directories = arguments[directory_index + 1:file_index]
        elif directory_index > file_index:
            if directory_index + 1 >= len(arguments):
                raise ValueError("Directory name is missing")
            directories = arguments[directory_index + 1:]
    else:
        if directory_index + 1 >= len(arguments):
            raise ValueError("Directory name is missing")
        directories = arguments[directory_index + 1:]
else:
    directories = []
if "-f" in arguments:
    file_index = arguments.index("-f")
    if file_index + 1 >= len(arguments):
        raise ValueError("File name is missing")
    file_name = arguments[file_index + 1]
way = ""
if len(directories) > 0:
    way = os.path.join(*directories)
    os.makedirs(way, exist_ok=True)
if "-f" in arguments:
    file_path = os.path.join(way, file_name)
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    timestamp = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    file_exist = os.path.exists(file_path)
    with open(file_path, "a") as file:
        if file_exist:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")
