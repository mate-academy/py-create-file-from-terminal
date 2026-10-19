import sys
import os
from datetime import datetime

dirs = []
file_name = None
i_value = 1
while i_value < len(sys.argv):
    if sys.argv[i_value] == "-d":
        i_value += 1
        while i_value < len(sys.argv) and sys.argv[i_value] != "-f":
            dirs.append(sys.argv[i_value])
            i_value += 1
    elif sys.argv[i_value] == "-f":
        i_value += 1
        if i_value < len(sys.argv):
            file_name = sys.argv[i_value]
            i_value += 1
    else:
        i_value += 1

if dirs:
    os.makedirs(os.path.join(*dirs), exist_ok=True)
if file_name:
    if dirs:
        file_path = os.path.join(*dirs, file_name)
    else:
        file_path = file_name

    lines = []
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        lines.append(content)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n")
        f.write(timestamp + "\n")
        for idx, line in enumerate(lines, 1):
            f.write(f"{idx} {line}\n")
