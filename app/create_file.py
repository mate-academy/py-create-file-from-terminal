import sys
import os
import datetime

l_path = sys.argv

f_count = len(l_path)
if "-f" in l_path:
    f_count = l_path.index("-f")

path = []
if "-d" in l_path:
    d_count = l_path.index("-d") + 1
    path = l_path[d_count:f_count]

current = datetime.datetime.now()
current = current.strftime("%y-%m-%d %H:%M:%S")


def write_to_file(patt):
    with open(patt, "a") as f:
        f.write(current + "\n")
        for line in sys.stdin:
            if line.rstrip() == "stop":
                break
            print(f"Enter content line: {line}")
            f.write(line)


if "-f" not in l_path:
    os.makedirs("app\\" + os.path.join(*path))
    open("app\\" + os.path.join(*path) + "\\" + "file.txt", "w")
    write_to_file("app\\" + os.path.join(*path) + "\\" + "file.txt")
if "-d" not in l_path:
    open("app\\" + l_path[-1], "w")
    write_to_file("app\\" + l_path[-1])
if "-d" in l_path and "-f" in l_path:
    os.makedirs("app\\" + os.path.join(*path))
    open("app\\" + os.path.join(*path) + "\\" + l_path[-1], "w")
    write_to_file("app\\" + os.path.join(*path) + "\\" + l_path[-1])
