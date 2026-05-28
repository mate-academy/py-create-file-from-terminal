import sys
import os
import datetime

dirs = []
filename = None

if "-d" in sys.argv:
    d_idx = sys.argv.index("-d")
    for i in range(d_idx + 1, len(sys.argv)):
        if sys.argv[i].startswith("-"):
            break
        dirs.append(sys.argv[i])

if "-f" in sys.argv:
    f_idx = sys.argv.index("-f")
    if f_idx + 1 < len(sys.argv):
        filename = sys.argv[f_idx + 1]

path = ""
if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

if filename:
    filepath = os.path.join(path, filename) if path else filename

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    file_exists = os.path.exists(filepath)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(timestamp + "\n")
        for i, text in enumerate(lines, 1):
            f.write(f"{i} {text}\n")