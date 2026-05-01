import sys
import os
from datetime import datetime

directories = None
filename = None

if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    f_index = sys.argv.index("-f") if "-f" in sys.argv else len(sys.argv)
    end = f_index if f_index > d_index else len(sys.argv)
    directories = sys.argv[d_index + 1 : end]

if "-f" in sys.argv:
    filename = sys.argv[sys.argv.index("-f") + 1]

if directories:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    if filename:
        filename = os.path.join(path, filename)

if filename:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(filename)

    with open(filename, "a") as file:
        if file_exists:
            file.write("\n")
        file.write(timestamp + "\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")
