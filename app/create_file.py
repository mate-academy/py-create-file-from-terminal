import sys
import os
from datetime import datetime


args = sys.argv
filename = None
dirs = []

if "-f" in args:
    if args.index("-f") + 1 < len(args):
        filename = args[args.index("-f") + 1]

if "-d" in args:
    start = args.index("-d")

    if "-f" in args and args.index("-f") > start:
        dirs = args[start + 1:args.index("-f")]
    else:
        dirs = args[args.index("-d") + 1:]


if filename:
    if dirs:
        os.makedirs(os.path.join(*dirs), exist_ok=True)
        full_path = os.path.join(*dirs, filename)
    else:
        full_path = filename

    with open(full_path, "a", encoding="utf-8") as f:
        now = datetime.now()
        f.write(now.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        counter = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{counter} {line}\n")
            counter += 1

else:
    if dirs:
        full_path = os.path.join(*dirs)
        os.makedirs(full_path, exist_ok=True)







