import os
import sys
from datetime import datetime


def writer(filename: str, path: str = None) -> None:
    if path:
        full_path = os.path.join(path, filename)
    else:
        full_path = filename
    with open(full_path, "a") as file:
        file.write(
            datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M:%S") + "\n"
        )
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n")
                break
            file.write(content + "\n")


arguments = sys.argv
path = None

if "-d" in arguments:
    path_index = arguments.index("-d") + 1
    if "-f" in arguments:
        file_index = arguments.index("-f")
        path = os.path.join(*arguments[path_index:file_index])
    else:
        path = os.path.join(*arguments[path_index:])
    os.makedirs(path, exist_ok=True)

if "-f" in arguments:
    filename = arguments[arguments.index("-f") + 1]
    writer(filename, path)
