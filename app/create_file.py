import argparse
import datetime
import os

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--dir", nargs="+", help="Create directory")
parser.add_argument("-f", "--file", help="File name")

command = vars(parser.parse_args())
path = ""

if command["dir"]:
    path = os.path.join(*command["dir"])
    os.makedirs(path, exist_ok=True)

with open(os.path.join(path, command["file"]), "a") as file:
    current_time = datetime.datetime.now()
    file.write(current_time.strftime("%y-%m-%d %H:%M:%S\n"))
    count = 0
    while (text := input("Enter content line: ")) != "stop":
        count += 1
        file.write(f"{count} " + text + "\n")
