from argparse import ArgumentParser
from os import path, makedirs
from datetime import datetime


parser = ArgumentParser()
parser.add_argument("-d", "--directory", nargs="*")
parser.add_argument("-f", "--file")
args = parser.parse_args()

if args.directory:
    makedirs(path.join(*args.directory), exist_ok=True)

if args.file:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

    if args.directory:
        args.file = path.join(*args.directory, args.file)

    with open(args.file, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for number, line in enumerate(lines):
            file.write(f"{number + 1} {line} \n")
        file.write("\n")
