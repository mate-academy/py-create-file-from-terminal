import datetime
import os
import sys


args = sys.argv[1:]

idx_d = args.index("-d") if "-d" in args else None
idx_f = args.index("-f") if "-f" in args else None

if idx_f is None or idx_f + 1 >= len(args):
    print("Error: file name is required after -f")
    sys.exit(1)
filename = args[idx_f + 1]

if idx_d is None:
    way = []
elif idx_f is None or idx_d > idx_f:
    way = args[idx_d + 1:]
else:
    way = args[idx_d + 1: idx_f]

if way:
    os.makedirs(os.path.join(*way), exist_ok=True)

file_path = os.path.join(*way, filename) if way else filename

with open(file_path, "a") as file:
    file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip() == "stop":
            break
        lines.append(line.rstrip())
    for i, line in enumerate(lines, 1):
        file.write(f"{i} {line}\n")
    file.write("\n")
