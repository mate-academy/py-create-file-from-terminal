import sys
import os
from datetime import datetime

args = sys.argv[1:]  # skip file name
path_parts = []
file_name = None

if "-d" in args:
    d_index = args.index("-d")
    # if -f is also, that directories are between -d and if
    if "-f" in args:
        f_index = args.index("-f")
        path_parts = args[d_index + 1:f_index]
    else:
        path_parts = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

# if directories are provided (-d), merge them in one path
directory_path = os.path.join(*path_parts) if path_parts else ""

# if file name is provided, join them to directory path
# if directory doesn't exist, path is just the same suck file name
full_path = os.path.join(directory_path, file_name)\
    if directory_path else file_name

# if directory exist, juz create him(with all parent tools, if necessary)
if directory_path:
    os.makedirs(directory_path, exist_ok=True)

lines = []
line_number = 1

while True:
    user_input = input("Enter content line:")
    if user_input.lower() == "stop":
        break
    lines.append(f"{line_number} {user_input}")
    line_number += 1

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
block = [timestamp] + lines  # timestamp as first line
block_content = "\n".join(block) + "\n"  # we are adding newline at the end

with open(full_path, "a", encoding="utf-8") as f:
    f.write(block_content)