import sys
import os
from datetime import datetime


args = sys.argv[1:]
directories = []
file_name = None


if "-d" in args:
    d_index = args.index("-d")

    next_flags = [
        i for i, arg in enumerate(args) if arg == "-f" and i > d_index
    ]

    if next_flags:
        directories = args[d_index + 1:next_flags[0]]
    else:
        directories = args[d_index + 1:]


if "-f" in args:
    f_index = args.index("-f")

    if f_index + 1 < len(args):
        file_name = args[f_index + 1]
    else:
        print("Error: missing filename after -f")
        sys.exit(1)


path = ""

if directories:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


if file_name is None:
    sys.exit(0)


if path:
    file_path = os.path.join(path, file_name)
else:
    file_path = file_name


lines = []

while True:
    line = input("Enter content line: ")

    if line == "stop":
        break

    lines.append(line)


timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


file_exists = os.path.exists(file_path) and os.path.getsize(file_path) > 0


with open(file_path, "a", encoding="utf-8") as output_file:

    if file_exists:
        output_file.write("\n")

    output_file.write(timestamp + "\n")

    for line_number, line in enumerate(lines, 1):
        output_file.write(f"{line_number} {line}\n")
