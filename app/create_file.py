import sys
import os
from datetime import datetime

args = sys.argv[1:]

if not args:
    print("Usage: python create_file.py -d dir1 dir2 -f filename.txt")
    sys.exit()

dirs = []
filename = None

if "-d" in args:
    d_index = args.index("-d")
    if "-f" in args:
        f_index = args.index("-f")
        dirs = args[d_index + 1:f_index]
    else:
        dirs = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")
    if f_index + 1 < len(args):
        filename = args[f_index + 1]
    else:
        print("Error: filename not provided")
        sys.exit()

path = ""
if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

if not filename:
    print(f"Directories created: {path}")
    sys.exit()

lines = []
while True:
    line = input("Enter content line (type 'stop' to finish): ")
    if line.lower() == "stop":
        break
    lines.append(line)

content = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"

for i, line in enumerate(lines, 1):
    content += f"{i}. {line}\n"

content += "\n"

file_path = os.path.join(path, filename) if path else filename

with open(file_path, "a", encoding="utf-8") as f:
    f.write(content)

print(f"File created/updated: {file_path}")
