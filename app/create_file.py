import sys
import os
from datetime import datetime


args = sys.argv


if "-d" in args and "-f" not in args:
    d_index = args.index("-d")
    directories = args[d_index + 1:]
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)

if "-f" in args and "-d" not in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]
    with open(file_name, "a") as f:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        line = 1
        while True:
            content = input(f"Enter content line: ")
            if content == "stop":
                break
            f.write(f"{line} {content}\n")
            line += 1

if "-d" in args and "-f" in args:
    d_index = args.index("-d")
    f_index = args.index("-f")
    if args.index("-d") > args.index("-f"):
        directories = args[d_index + 1:]
        file_name = args[f_index + 1]
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)
    else:
        file_name = args[f_index + 1]
        directories = args[d_index + 1: f_index]
        path = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)

    with open(os.path.join(path, file_name), "a") as f:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        line = 1
        while True:
            content = input(f"Enter content line: ")
            if content == "stop":
                break
            f.write(f"{line} {content}\n")
            line += 1
