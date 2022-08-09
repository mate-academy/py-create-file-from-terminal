import os
import sys
from datetime import datetime


today = datetime.now()
dat_list = str(today).split(".")
dat = dat_list[0]


def creater():
    with open("file.txt", "a") as f:
        f.write(dat + "\n")
        print(os.getcwd())
        for line in sys.stdin:
            print(f'Enter content line: {line}')
            d = line.replace('stop', '')
            f.write(d)
            if 'stop' == line.rstrip():
                break


if "-d" in sys.argv and "-f" not in sys.argv:
    os.makedirs("dir1/dir2")


if "-f" in sys.argv and "-d" not in sys.argv:
    creater()

if "-d" in sys.argv and "-f" in sys.argv:
    os.makedirs("dir1/dir2")
    os.chdir("dir1")
    os.chdir("dir2")
    creater()
