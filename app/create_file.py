import os
import sys
import datetime


args = sys.argv
path = os.getcwd

if "-d" in args:
    for i in range(args.index("-d") + 1, len(args)):
        if i == "-f":
            break
        path = os.path.join(path, args[i], "")
        os.makedirs(path)

if "-f" in args:
    with open(os.path.join(path, args[args.index("-f") + 1]), "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n")
        line_number = 1
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                break
            f.write(f"{line_number} {input_line} \n")
            line_number += 1
