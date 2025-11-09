import os
import sys
import datetime

arguments = sys.argv
if "-f" in arguments:
    filename = arguments[arguments.index("-f") + 1]

if "-d" in arguments:
    directory = arguments[arguments.index("-d") + 1 : arguments.index("-f")]
    os.makedirs(os.path.join(*directory), exist_ok=True)
    filepath = os.path.join(*directory, filename)
else:
    filepath = filename

lines = []
while True:
    line = input("Enter content line: ")
    if line.strip().lower() == "stop":
        break
    lines.append(line)

with open(filepath, "a", encoding="utf-8") as f:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"\n{timestamp}\n")
    for i, line in enumerate(lines, start=1):
        f.write(f"{i} {line}\n")
