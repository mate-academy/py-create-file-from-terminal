import os
from sys import argv
from datetime import datetime

if "-d" in argv and "-f" in argv:
    path = ""
    for directory in argv[2:argv.index("-f")]:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            os.mkdir(path)
    file_name = argv[argv.index("-f") + 1]
    path = os.path.join(path, file_name)
    with open(path, "a") as file_w:
        date = datetime.now()
        file_w.write(date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            content = input("Enter content line (type 'stop' to finish): ")
            if content == "stop":
                break
            file_w.write(content + "\n")
if argv[1] == "-d":
    path = ""
    for directory in argv[2:]:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            os.mkdir(path)
elif argv[1] == "-f":
    with open(argv[2], "a") as file_w:
        date = datetime.now()
        file_w.write(date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            content = input("Enter content line (type 'stop' to finish): ")
            if content == "stop":
                break
            file_w.write(content + "\n")
