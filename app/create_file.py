import os
import sys

from datetime import datetime

argv = sys.argv


def create_folder() -> list:
    if "-f" in argv and argv.index("-d") < argv.index("-f"):
        dirs = argv[argv.index("-d") + 1:argv.index("-f")]
    else:
        dirs = argv[argv.index("-d") + 1:]
    os.makedirs(os.path.join(*dirs), exist_ok=True)
    return dirs


def create_file() -> None:
    if "-d" in argv:
        path = create_folder()
    else:
        path = ""
    file_name = os.path.join(*path, argv[argv.index("-f") + 1])
    with open(file_name, "a") as f:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write("\n" + time_now + "\n")
        num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            f.write(f"{num} {line}\n")
            num += 1


if "-d" in argv:
    create_folder()
if "-f" in argv:
    create_file()
