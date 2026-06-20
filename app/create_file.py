import datetime
import os
import sys

args = sys.argv[1:]

# find flags

d_index = args.index("-d") if "-d" in args else None
f_index = args.index("-f") if "-f" in args else None

# extract file name

file_name = None
if f_index is not None and f_index + 1 < len(args):
    file_name = args[f_index + 1]

# extract directory

directory = []

if d_index is not None:
    end_index = len(args)

    if f_index is not None and f_index > d_index:
        end_index = f_index

    directory = args[d_index + 1:end_index]

dir_path = os.path.join(*directory) if directory else "."

# create directory if needed
if directory:
    os.makedirs(dir_path, exist_ok=True)

# read input lines
if file_name is not None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    # format content

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_lines = [
        f"{number} {line}"
        for number, line in enumerate(lines, start=1)
    ]

    new_block = timestamp + "\n" + "\n".join(formatted_lines)

    # file path

    file_path = os.path.join(dir_path, file_name)

    if os.path.exists(file_path):
        mode = "a"
        content = "\n\n" + new_block
    else:
        mode = "w"
        content = new_block

    with open(file_path, mode) as f:
        f.write(content)
