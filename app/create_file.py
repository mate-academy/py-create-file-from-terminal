import os
import argparse
from datetime import datetime


parser = argparse.ArgumentParser()

parser.add_argument("-d", "--directory", type=str, nargs="+")
parser.add_argument("-f", "--filename", type=str)

args = parser.parse_args()

if args.directory:
    directory_path = os.path.join(*args.directory)
    os.makedirs(directory_path)
else:
    directory_path = os.getcwd()

filepath = os.path.join(directory_path, args.filename)

with open(filepath, "a") as file:
    file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        file.write(content + "\n")
