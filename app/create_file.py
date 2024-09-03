import os
import sys
import datetime


args = sys.argv
dirs = ""

if "-d" in args:
    if args.index("-d") > args.index("-f") or "-f" not in args:
        dirs = "/".join(args[args.index("-d") + 1:]) + "/"
    else:
        dirs = "/".join(args[args.index("-d") + 1:args.index("-f")]) + "/"

    if not os.path.exists(dirs):
        os.makedirs(dirs)

if "-f" in args:
    with open(dirs + args[args.index("-f") + 1], "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        while True:
            string = input("Enter content line: ")
            if string == "stop":
                break
            file.write(string + "\n")
