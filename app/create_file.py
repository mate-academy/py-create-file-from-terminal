import sys
import os
from datetime import datetime


args = sys.argv[1:]

directories = []
filename = None

i = 0

while i < len(args):
    if args[i] == "-d":
        i += 1

        while i < len(args) and args[i] not in ("-d", "-f"):
            directories.append(args[i])
            i += 1

    elif args[i] == "-f":
        filename = args[i + 1]
        i += 2

    else:
        i += 1

directory_path = ""

if directories:
    directory_path = os.path.join(*directories)
    os.makedirs(directory_path, exist_ok=True)

if filename:
    if directories:
        file_path = os.path.join(directory_path, filename)
    else:
        file_path = filename

    lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(timestamp + "\n")

        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")
