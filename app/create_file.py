import sys
import os
import datetime


dirs = []
filename = None
if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    f_index = sys.argv.index("-f") if "-f" in sys.argv else len(sys.argv)
    dirs = sys.argv[d_index + 1:f_index]
if "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    filename = sys.argv[f_index + 1]
print("Dirs:", dirs)
print("Filename:", filename)

if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

lines = []
while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)

if dirs:
    filepath = os.path.join(*dirs, filename)
else:
    filepath = filename

with open(filepath, "a") as f:
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    for i, line in enumerate(lines, 1):
        f.write(f"{i} {line}\n")
