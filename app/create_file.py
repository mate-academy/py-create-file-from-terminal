import sys
import os
from datetime import datetime

print(sys.argv)

has_d = "-d" in sys.argv
has_f = "-f" in sys.argv

dirs = []
file_name = None

if has_d:
    d_index = sys.argv.index("-d")

    if has_f:
        f_index = sys.argv.index("-f")
        dirs = sys.argv[d_index + 1:f_index]
    else:
        dirs = sys.argv[d_index + 1:]

if has_f:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]

print("dirs:", dirs)
print("file_name", file_name)


if not file_name:
    print("Error: file name is required (-f)")
    sys.exit(1)

if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    full_path = os.path.join(path, file_name)
else:
    full_path = file_name

lines = []
while True:
    line = input("enter content line: ")
    if line == "stop":
        break
    lines.append(line)

numbered_lines = []
for i, line in enumerate(lines, start=1):
    numbered_lines.append(f"{i} {line}")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content = []
content.append(timestamp)
content.extend(numbered_lines)

with open(full_path, "a") as f:
    f.write("\n".join(content) + "\n")
