import argparse
import os


from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("-d", nargs="*")
parser.add_argument("-f", nargs="*")

args = parser.parse_args()
path = args.d
file_name = args.f

current = os.getcwd()
if path:
    for i in range(len(path)):
        current = os.path.join(current, path[i])
        if not os.path.isdir(current):
            os.mkdir(current)

if file_name:
    if path:
        file_name = [os.path.join(current, *file_name)]
    with open(*file_name, "a+") as file:
        if os.path.getsize(*file_name):
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line = 0
        while True:
            content = input("Enter content line: ")
            line += 1
            if content == "stop":
                break
            file.write(f"{line} {content}\n")
