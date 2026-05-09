import sys
import os
from datetime import datetime

args = sys.argv[1:]

dirs = []
filename = None
current_flag = None
for arg in args:
    if arg == "-d":
        current_flag = "-d"
    elif arg == "-f":
        current_flag = "-f"
    else:
        if current_flag == "-d":
            dirs.append(arg)

        elif current_flag == "-f" and filename is None:
            filename = arg

dir_path = ""

if dirs:
    dir_path = os.path.join(*dirs)
    os.makedirs(dir_path, exist_ok=True)

if filename:
    file_path = os.path.join(dir_path, filename)

    lines = []

    while True:
        content = input("Enter content line: ")

        if content == "stop":
            break

        lines.append(content)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(f"{timestamp}\n")

        for index, line in enumerate(lines, start=1):
            file.write(f"{index} {line}\n")
