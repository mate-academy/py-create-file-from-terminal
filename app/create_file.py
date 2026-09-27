import os
import sys
from datetime import datetime


args = sys.argv[1:]

file_name = None
directories = []

if "-f" in args:
    file_index = args.index("-f")
    if file_index + 1 < len(args):
        file_name = args[file_index + 1]

if "-d" in args:
    dir_index = args.index("-d")
    end_index = len(args)

    if "-f" in args and args.index("-f") > dir_index:
        end_index = args.index("-f")

    directories = args[dir_index + 1:end_index]

if directories:
    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)
else:
    directory_path = "."

if file_name:
    file_path = os.path.join(directory_path, file_name)

    content_lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for number, line in enumerate(content_lines, start=1):
            file.write(f"{number} {line}\n")
