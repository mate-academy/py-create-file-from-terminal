import sys
import os
from datetime import datetime


args = sys.argv[1:]
dirs = []
file_name = None


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
        file_name = args[f_index + 1]
    else:
        print("Error: missing filename after -f")
        sys.exit(1)


path = ""

if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)


if file_name:
    if path:
        file_path = os.path.join(path, file_name)
    else:
        file_path = file_name
else:
    print("File name not provided")
    sys.exit(1)


lines = []

while True:
    line = input("Enter content line: ")

    if line == "stop":
        break

    lines.append(line)


timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0


with open(file_path, "a", encoding="utf-8") as f:

    if file_exists:
        f.write("\n")

    f.write(timestamp + "\n")

    for i, line in enumerate(lines, 1):
        f.write(f"{i} {line}\n")
