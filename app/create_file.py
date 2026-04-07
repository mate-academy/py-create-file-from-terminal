import sys
import os
from datetime import datetime

args = sys.argv

if "-f" not in args:
    print("Error: -f flag is required")
    sys.exit(1)

file_index = args.index("-f") + 1
filename = args[file_index]

path = "."

if "-d" in args:
    d_index = args.index("-d") + 1

    dirs = []
    for arg in args[d_index:]:
        if arg == "-f":
            break
        dirs.append(arg)

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

full_path = os.path.join(path, filename)

lines = []

while True:
    text = input("Enter content line: ")
    if text == "stop":
        break
    lines.append(text)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

content = timestamp + "\n"

for i, line in enumerate(lines, 1):
    content += f"{i} {line}\n"

if os.path.exists(full_path):
    content = "\n" + content

with open(full_path, "a") as f:
    f.write(content)

print(f"File created: {full_path}")
