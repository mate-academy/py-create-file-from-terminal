import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-d", dest="dir", nargs="*", help="Creates a directory")
parser.add_argument("-f", dest="file", help="Creates a file")

args = parser.parse_args()


def create_dir(directory: str) -> None:
    os.makedirs(f"{directory}", exist_ok=True)


def create_file(file_name: str, content: list) -> None:
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(f"{file_name}", "a") as f:
        f.write(f"{date}\n")
        for index, text in enumerate(content, start=1):
            f.write(f"{index} {text}\n")
        f.write("\n")


if args.dir:
    path = os.path.join(*args.dir)
    create_dir(str(path))

if args.file:
    lines = []

    while True:
        line = input("Input content line: ")
        if line == "stop":
            break
        lines.append(line)

    if args.dir:
        file_path = os.path.join(*args.dir, str(args.file))
    else:
        file_path = args.file

    create_file(file_path, lines)
