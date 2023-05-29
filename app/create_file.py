import os
import sys
from datetime import datetime


args = sys.argv


if "-d" in args:
    if "-f" in args:
        path = os.path.join(*args[args.index("-d") + 1:args.index("-f")])
    else:
        path = os.path.join(*args[args.index("-d") + 1:])
    os.makedirs(path, exist_ok=True)

if "-f" in args:
    if "-d" in args:
        file_name = os.path.join(path, args[-1])
    else:
        file_name = args[-1]
    with open(file_name, "a") as new_file:
        new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line = input("Enter content line: ")
        page_number = 1
        while True:
            new_file.write(f"{page_number} {line}\n")
            page_number += 1
            line = input("Enter content line: ")
            if line == "stop":
                new_file.write("\n")
                break
