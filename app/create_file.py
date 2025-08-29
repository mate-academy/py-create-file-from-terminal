import sys
import os
import datetime


args = sys.argv
if "-d" in args and "-f" not in args:
    os.makedirs(os.path.join(args[2:]))
if "-d" not in args and "-f" in args:
    with open(args[2], "a") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        f.write(time)
        text = input("Enter content line: ")
        while text != "stop":
            text += "\n"
            f.write(text)
            text = input("Enter content line: ")
        f.write("\n")

if "-d" in args and "-f" in args:
    f_index = args.index("-f")
    d_index = args.index("-d")
    if f_index > d_index:
        path = os.path.join(*args[2:f_index])
        os.makedirs(path)
        with open(os.path.join(path, args[f_index + 1]), "a") as f:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            f.write(time)
            text = input("Enter content line: ")
            while text != "stop":
                text += "\n"
                f.write(text)
                text = input("Enter content line: ")
            f.write("\n")
    if f_index < d_index:
        path = os.path.join(args[4:])
        os.makedirs(path)
        with open(os.path.join(path, args[f_index + 1]), "a") as f:
            time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
            f.write(time)
            text = input("Enter content line: ")
            while text != "stop":
                text += "\n"
                f.write(text)
                text = input("Enter content line: ")
            f.write("\n")
