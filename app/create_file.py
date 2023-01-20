import sys
import os
from datetime import datetime

if "-d" in sys.argv and "-f" in sys.argv:
    path_string = ""
    for direction in sys.argv[sys.argv.index("-d") + 1: len(sys.argv) - 2]:
        path_string += f"{direction}/"
        if not os.path.isdir(path_string):
            os.mkdir(path_string)

    with open(path_string + sys.argv[-1], "a") as new_file:
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        new_file.write(date_time)
        i = 0
        line = ""
        while line != "stop":
            new_file.write(f"{i} {line}")
            new_file.write("\n")
            i += 1
            line = input("Enter content line: ")


if "-d" in sys.argv and "-f" not in sys.argv:
    path_string = ""
    for direction in sys.argv[sys.argv.index("-d") + 1: len(sys.argv)]:
        path_string += f"{direction}/"
        if not os.path.isdir(path_string):
            os.mkdir(path_string)

if "-f" in sys.argv and "-d" not in sys.argv:
    with open(sys.argv[-1], "a") as new_file:
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        new_file.write(date_time)
        i = 0
        line = ""
        while line != "stop":
            new_file.write(f"{i} {line}")
            new_file.write("\n")
            i += 1
            line = input("Enter content line: ")
