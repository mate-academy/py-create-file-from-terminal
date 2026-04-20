import sys
import os
from datetime import datetime


def write_content(patch: str) -> None:
    total = 0
    with open(patch, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            line = input("Enter content line:")
            if line == "stop":
                break
            total += 1
            file.write(f"{total} {line}\n")


if sys.argv[1] == "-f":
    filename = sys.argv[2]
    write_content(filename)


if sys.argv[1] == "-d":
    folders = sys.argv[2:]

    if "-f" in folders:
        index = folders.index("-f")
        folders_only = folders[:index]
        filename = folders[index + 1]

        if len(folders_only) == 1:
            path = os.path.join(*folders_only)
            os.makedirs(path, exist_ok=True)
            full_path = os.path.join(path, filename)

        else:
            path = os.path.join(*folders_only)
            os.makedirs(path, exist_ok=True)
            full_path = os.path.join(path, filename)
        write_content(full_path)
    else:
        path = os.path.join(*folders)
        os.makedirs(path, exist_ok=True)
