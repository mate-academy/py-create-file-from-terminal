import sys
import os
from datetime import datetime


list_args = sys.argv
list_args = list_args[slice(1, len(list_args))]
directories = []
flags = False
for arg in list_args:
    if str(arg).startswith("-"):
        if arg == "-d" or arg == "-f":
            flags = True
        else:
            raise Exception("Flag into args is incorrect")

    if (arg != "-d") and (arg != "-f") and flags:
        directories.append(arg)
if len(directories) > 1:
    os.makedirs(os.path.join(*directories[: -1]))
with open(os.path.join(*directories), "a") as out_file:
    time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    out_file.write(time + "\n")
    count = 1
    while True:
        value = input("Enter content line:")
        if value == "stop":
            break
        out_file.write(str(count) + " " + value + "\n")
        count += 1
