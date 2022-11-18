import argparse
import os
from datetime import datetime as dt

parser = argparse.ArgumentParser()

parser.add_argument("-d", type=str,
                    default=[],
                    nargs="*",
                    help="all items after this flag are parts of the path")
parser.add_argument("-f", type=str,
                    help="first item is the file name")
args = parser.parse_args()

path = args.d
file_name = args.f
directory = ""

for i in range(len(path)):
    directory = os.path.join(directory, path[i])
    if os.path.isfile(directory):
        os.mkdir(directory)
directory = os.path.join(directory, file_name)
with open(directory, "a") as file:
    now = dt.now()
    file.write(now.strftime("%Y-%m-%d %H:%M:%S \n"))
    line_number = 1
    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        file.write(f"{line_number} {content_line} \n")
        line_number += 1
