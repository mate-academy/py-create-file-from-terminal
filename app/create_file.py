import os
import argparse
from datetime import datetime


parser = argparse.ArgumentParser()

parser.add_argument("-d", dest="dir", nargs="*")
parser.add_argument("-f", dest="file", nargs="*")

args = parser.parse_args()

path = ""

if args.dir:
    path = os.path.join(*args.dir)
    os.makedirs(path, exist_ok=True)

if args.file:
    if path:
        path += "/"
    with open(path + args.file[0], "a") as file:
        file.write(datetime.now().strftime("%Y-%d-%m %H:%M:%S\n"))
        line_num = 1
        line_in = input("Enter content line: ")
        while line_in != "stop":
            file.write(f"{line_num} {line_in}\n")
            line_in = input("Enter content line: ")
            line_num += 1
        file.write("\n")
