import sys
import os
from datetime import datetime


directories = []
filename = None
if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    end_index = len(sys.argv)
    for flag in ["-f"]:
        if flag in sys.argv and sys.argv.index(flag) > d_index:
            end_index = sys.argv.index(flag)
    directories = sys.argv[d_index + 1:end_index]
if "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    filename = sys.argv[f_index + 1]

if directories:
    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)
    if filename is not None:
        file_path = os.path.join(directory_path, filename)
else:
    file_path = filename

if filename is not None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = timestamp + "\n"
    for number, line in enumerate(lines, start=1):
        content += f"{number} {line}\n"
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        content = "\n" + content
    with open(file_path, "a") as file:
        file.write(content)
