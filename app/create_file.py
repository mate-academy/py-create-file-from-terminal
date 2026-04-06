import sys
import os
from datetime import datetime


args = sys.argv[1:]
dir_parts = []
file_name = None

if not args:
    print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
    sys.exit(1)

if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        dir_parts = args[d_index + 1:f_index]
    else:
        dir_parts = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 < len(args):
        file_name = args[f_index + 1]
    else:
        print("Error: File name not provided after -f")
        sys.exit(1)

current_path = os.getcwd()

if dir_parts:
    dir_path = os.path.join(current_path, *dir_parts)
    os.makedirs(dir_path, exist_ok=True)
else:
    dir_path = current_path

if file_name:
    file_path = os.path.join(dir_path, file_name)
    lines = []

    while True:
        user_input = input("Enter content line: ")
        if user_input == "stop":
            break
        lines.append(user_input)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    content_to_write = []

    if os.path.exists(file_path):
        content_to_write.append("\n")

    content_to_write.append(timestamp + "\n")

    for i, line in enumerate(lines, start=1):
        numbered_line = f"{i} {line}\n"
        content_to_write.append(numbered_line)

    with open(file_path, "a", encoding="utf-8") as f:
        f.writelines(content_to_write)

    print(f"File created/updated at: {file_path}")
