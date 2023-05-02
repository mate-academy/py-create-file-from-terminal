import os
import sys
from datetime import datetime


argv = sys.argv
now = datetime.now()


def create_folder() -> list:
    if "-f" in argv and argv.index("-d") < argv.index("-f"):
        dirs = argv[argv.index("-d") + 1:argv.index("-f")]
    else:
        dirs = argv[argv.index("-d") + 1:]
    os.makedirs(os.path.join(*dirs), exist_ok=True)
    return dirs


def create_file() -> None:
    if "-d" in argv:
        folders = create_folder()
        file_name = argv[argv.index("-f") + 1]
        file_path = os.path.join(*folders, file_name)
    else:
        file_path = argv[argv.index("-f") + 1]
    with open(file_path, "a") as file_sample:
        file_sample.write("\n" + now.strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        number = 1
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            else:
                file_sample.write(f"{number} {text}\n")
                number += 1


if "-d" in argv:
    create_folder()
if "-f" in argv:
    create_file()
