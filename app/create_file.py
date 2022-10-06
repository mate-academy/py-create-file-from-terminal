import argparse
import os
import datetime


parser = argparse.ArgumentParser()

parser.add_argument("-d", "--dir", nargs="+", help="Create directory")
parser.add_argument("-f", "--file", help="File name")

command = vars(parser.parse_args())
path = ""
print(command, type(command), path)

if command["dir"]:
    path = os.path.join(*command["dir"])
    os.makedirs(path)

print(command, type(command), path)

with open(os.path.join(path, command["file"]), "w") as file:
    current_time = datetime.datetime.now()
    file.write(current_time.strftime("%y-%m-%d %H:%M:%S") + "\n")
    while True:
        text = input("Enter content line: ")
        if text == "stop":
            break
        file.write(text + "\n")
