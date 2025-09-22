import datetime
import sys
import os


args = sys.argv[1:]

dirs: list = []
file_name: str | None = None

if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")
        dirs = args[d_index + 1: f_index]
    else:
        dirs = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

if dirs:
    dir_path : str = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, file_name)
else:
    file_path = file_name

lines = []
while True:
    line = input("Enter content line: ")
    if line.lower() == "stop":
        break
    lines.append(line)

with open(f"{file_path}", "a") as f:
    timestamp = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    f.write(timestamp + "\n")

    for i, line in enumerate(lines, start=1):
        f.write(f"{i} {line}\n")

    f.write("\n")
