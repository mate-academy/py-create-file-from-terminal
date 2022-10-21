import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="File name")
parser.add_argument("-d", "--dir", nargs="+", help="Path")
command = parser.parse_args()


if command.dir:
    path_ = os.path.join(*command.dir)
    os.makedirs(path_, exist_ok=True)
    os.chdir(path_)


if command.file:
    content = []
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content.append(content_line)

    with open(command.file, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for idx, line in enumerate(content, start=1):
            file.write(f"{idx} {line}\n")
