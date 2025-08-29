import sys
import os
import datetime


def write_text(file) -> None:
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    index = 1
    f.write(time)
    text = input("Enter content line: ")
    while text != "stop":
        text = str(index) + " " + text + "\n"
        index += 1
        f.write(text)
        text = input("Enter content line: ")
    f.write("\n")


args = sys.argv
if "-d" in args and "-f" not in args:
    os.makedirs(os.path.join(*args[2:]), exist_ok=True)
if "-d" not in args and "-f" in args:
    with open(args[2], "a") as f:
        write_text(f)

if "-d" in args and "-f" in args:
    f_index = args.index("-f")
    d_index = args.index("-d")
    if f_index > d_index:
        path = os.path.join(*args[2:f_index])
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, args[f_index + 1]), "a") as f:
            write_text(f)
    if f_index < d_index:
        path = os.path.join(*args[4:])
        os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, args[f_index + 1]), "a") as f:
            write_text(f)
