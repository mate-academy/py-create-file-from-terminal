from datetime import datetime
import os
import sys

args = sys.argv[1:]

dir_parts = []
file_name = None

if "-d" in args:
    d_idx = args.index("-d")
    for arg in args[d_idx + 1:]:
        if arg.startswith("-"):
            break
        dir_parts.append(arg)

if "-f" in args:
    f_idx = args.index("-f")
    if f_idx + 1 < len(args):
        file_name = args[f_idx + 1]

if dir_parts:
    os.makedirs(os.path.join(*dir_parts), exist_ok=True)

if file_name:
    target_path = (
        os.path.join(*dir_parts, file_name) if dir_parts else file_name
    )

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists_and_not_empty = (
        os.path.exists(target_path) and os.path.getsize(target_path) > 0
    )

    with open(target_path, "a") as file:
        if file_exists_and_not_empty:
            file.write("\n")
        file.write(f"{timestamp}\n")
        for index, content in enumerate(lines, start=1):
            file.write(f"{index} {content}\n")
