import sys
import os
from datetime import datetime


arguments = sys.argv[1:]
name = "tittle_was_not_supplied"
directory = ["directory", "was", "not", "supplied"]

if "-f" in arguments and "-d" in arguments:
    f_index = arguments.index("-f")
    d_index = arguments.index("-d")
    name = arguments[f_index + 1]
    if f_index < d_index:
        directory = arguments[d_index + 1:]
    else:
        directory = arguments[d_index + 1: f_index]
elif "-f" in arguments:
    f_index = arguments.index("-f")
    name = arguments[f_index + 1]
elif "-d" in arguments:
    d_index = arguments.index("-d")
    directory = arguments[d_index + 1:]

path = os.path.join(*directory)
os.makedirs(path, exist_ok=True)

with open(path + "\\" + name, "a+") as f:
    f.writelines(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n")
    i = 1
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        f.writelines(str(i) + " " + content + "\n")
        i += 1
    f.write("\n")
