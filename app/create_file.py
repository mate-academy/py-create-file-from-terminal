import os
import sys
from datetime import datetime


def create_path(dir_flag: (int, None),
                file_flag: (int, None),
                args: list) -> str:
    if file_flag and file_flag > dir_flag:
        dirs = args[dir_flag + 1:file_flag]
    else:
        dirs = args[dir_flag + 1:]
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)
    return path


def file_content(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        count = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{count} {line}\n")
            count += 1


args = sys.argv
dir_flag = args.index("-d") if "-d" in args else None
file_flag = args.index("-f") if "-f" in args else None
path = ""
if dir_flag:
    path = create_path(dir_flag, file_flag, args)
if file_flag:
    file_path = os.path.join(path, args[file_flag + 1])
    file_content(file_path)
