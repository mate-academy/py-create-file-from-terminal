import sys
import os
from datetime import datetime


if "-d" in sys.argv and "-f" in sys.argv:
    path = ""
    for directory in sys.argv[sys.argv.index("-d") + 1: len(sys.argv) - 2]:
        path += f"{directory}/"
        if not os.path.isdir(path):
            os.mkdir(path)

    with open(path + sys.argv[-1], "a") as f:
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(date_time)
        i = 0
        line = ""
        while line != "stop":
            f.write(f"{i} {line} \n")
            i += 1
            line = input("Enter content line: ")


if "-d" in sys.argv and "-f" not in sys.argv:
    path = ""
    for directory in sys.argv[sys.argv.index("-d") + 1: len(sys.argv)]:
        path += f"{directory}/"
        if not os.path.isdir(path):
            os.mkdir(path)

if "-f" in sys.argv and "-d" not in sys.argv:
    with open(sys.argv[-1], "a") as f:
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(date_time)
        i = 0
        line = ""
        while line != "stop":
            f.write(f"{i} {line} \n")
            i += 1
            line = input("Enter content line: ")
