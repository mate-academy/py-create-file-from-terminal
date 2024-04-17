import os
import sys
from datetime import datetime

args = sys.argv[1:]
if not args:
    print("Usage: python create_file.py [-d directory] [-f filename]")
    exit()

f_index = None
path_index = None
path = None
filename = None

if "-f" in args:
    f_index = args.index("-f")
    filename = args[f_index + 1]
if "-d" in args:
    path_index = args.index("-d") + 1
    if f_index:
        path = os.path.join(*args[path_index: f_index])
    else:
        path = os.path.join(*args[path_index:])

if path:
    os.makedirs(path, exist_ok=True)
if filename:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path = os.path.join(path, filename) if path else filename
    file_exists = os.path.exists(file_path)
    content = []
    with open(file_path, "a") as file:
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content.append(line)
        if file_exists:
            file.write("\n")
        file.write(timestamp + "\n")
        for idx, line in enumerate(content, start=1):
            file.write(f"{idx} {line}\n")
