import os
import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Usage: python script.py -d <dir1> <dir2> -f <file_name>")
    sys.exit(1)

dirs = []
file_name = None
i = 1

while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == "-d":
        i += 1
        while i < len(sys.argv) and not sys.argv[i].startswith("-"):
            dirs.append(sys.argv[i])
            i += 1
    elif arg == "-f":
        if i + 1 < len(sys.argv):
            file_name = sys.argv[i + 1]
            i += 2
        else:
            print("Error: -f requires a filename")
            sys.exit(1)
    else:
        i += 1

if file_name is None:
    print("Error: filename is required (-f)")
    sys.exit(1)

# Створення шляху
if dirs:
    dir_path = os.path.join(*dirs)
else:
    dir_path = ""  # This line must be indented

os.makedirs(dir_path, exist_ok=True)
full_path = os.path.join(dir_path, file_name)

# Збір контенту
content = []
print("Enter content lines (type 'stop' to finish):")
while True:
    line = input("Enter content line: ")
    if line.lower() == "stop":
        break
    content.append(line)

# Запис у файл (один раз)
if os.path.exists(full_path):
    with open(full_path, "a", encoding="utf-8") as f:
        f.write("\n")
ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(full_path, "a", encoding="utf-8") as f:
    f.write(f"{ts}\n")
    for idx, line in enumerate(content, 1):
        f.write(f"{idx} {line}\n")

print(f"\nFile saved to: {full_path}")
