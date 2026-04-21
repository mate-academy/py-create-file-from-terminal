import os
import sys
from datetime import datetime

arguments = list(sys.argv)
arguments.pop(0)

directory_parts = []
target_file = None

if "-d" in arguments:
    args_after_d = arguments[arguments.index("-d") + 1:]
    for arg in args_after_d:
        if arg == "-f":
            break
        directory_parts.append(arg)

if "-f" in arguments:
    args_after_f = arguments[arguments.index("-f") + 1:]
    if args_after_f:
        target_file = args_after_f[0]

directory_path = ""
if directory_parts:
    directory_path = directory_parts[0]
    for part in directory_parts[1:]:
        directory_path = os.path.join(directory_path, part)

if directory_path:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

lines_buffer = []
if target_file:
    while True:
        user_input = input("Enter content line: ")
        if user_input.strip().lower() == "stop":
            break
        lines_buffer.append(user_input)

if target_file:
    file_path = os.path.join(directory_path, target_file)
    is_existing_file = os.path.exists(file_path)
    with open(file_path, "a") as file:
        if is_existing_file:
            file.write("\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        for line_number, text in enumerate(lines_buffer):
            file.write(f"{line_number + 1} {text}\n")
