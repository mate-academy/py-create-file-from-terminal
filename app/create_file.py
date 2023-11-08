from sys import argv
from os import makedirs
from os import path
from datetime import datetime


f_index = argv.index("-f")
path_to_file = ""

if "-d" in argv:
    d_index = argv.index("-d")
    path_to_file = "/".join(argv[d_index + 1: f_index])
    if not path.exists(path_to_file):
        makedirs(path_to_file)


name = argv[f_index + 1]
with open(path_to_file + "/" + name, "w") as f:
    f.write(datetime.now().strftime("%Y/%m/%d, %H:%M:%S") + "\n")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        f.write(line + "\n")
