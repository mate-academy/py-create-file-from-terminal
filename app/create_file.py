import argparse
import datetime
import os
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', nargs='*')
    parser.add_argument('-f', '--file', nargs='*')
    return parser


parser = create_parser()
args = parser.parse_args(sys.argv[1:])
path = ""
dir_list = list(args.dir)
for arg in dir_list:
    path = os.path.join(path, arg)
    os.mkdir(path)
filename = args.file[0]
dt = datetime.datetime.now()

content = []
line_string = ""
while line_string != "stop":
    line_string = input("Enter content line: ")
    if line_string == "stop":
        break
    content.append(line_string + "\n")
with open(os.path.join(path, filename), "w") as file:
    file.write(dt.strftime('%Y-%m-%d %H:%M:%S') + "\n")
    n = 1
    for line in content:
        file.write(f"{n} {line}")
