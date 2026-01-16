import datetime
import os
import sys


args = sys.argv[1:]

if "-d" in sys.argv:
    way = args[sys.argv.index("-d")+1:] or args[sys.argv.index("-d")+1: sys.argv.index("-f")]




    with open(args[1], "a") as file:
        file.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
        while True:
            if sys.argv == "stop":
                break
        line_number = 1
        file.write(line_number + sys.argv)
        line_number += 1