import os
import sys
import datetime


args = sys.argv

if "-d" in args and "-f" in args:
    dir_list = "/".join(
        args[args.index("-d") + 1:args.index("-f")]) + "/" \
        if "-d" in args else ""
else:
    dir_list = "/".join(
        args[args.index("-d") + 1:]) + "/" if "-d" in args else ""

if len(dir_list) > 0:
    if not os.path.exists(dir_list):
        os.makedirs(dir_list)

if "-f" in args:
    with open(dir_list + args[-1], "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        while True:
            string = input("Enter content line: ")
            if string == "stop":
                break
            file.write(string + "\n")
