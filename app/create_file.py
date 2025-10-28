import sys
import os
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    directory = []
    file_name = None
    mode = None

    for arg in args:
        if arg == "-d":
            mode = "dir"
        elif arg == "-f":
            mode = "file"
        else:
            if mode == "dir":
                directory.append(arg)
            elif mode == "file" and file_name is None:
                file_name = arg
    if file_name:
        if not directory:
            full_path = file_name
        else:
            folder_path = os.path.join(*directory)
            full_path = os.path.join(folder_path, file_name)

        if directory:
            os.makedirs(folder_path, exist_ok=True)

        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(full_path, "a") as f:
            f.write(timestamp + "\n")
            for i, line in enumerate(lines, start=1):
                f.write(f"{i}. {line}\n")
            f.write("\n")
