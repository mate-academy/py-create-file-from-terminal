import os
import sys
import datetime

mode = "f"
inp = sys.argv


def mkdir(path: str) -> None:
    if path != "-f":
        cwd = os.getcwd()
        os.mkdir(path)
        os.chdir(cwd + "\\" + path)


def mkfile(name: str) -> object:
    fil = open(name, "a")
    return fil


for _ in inp:
    if _ == "-d":
        mode = "d"
    if _ == "-f":
        mode = "f"
    if _ not in ["-f", "-d"] and mode == "f":
        fil = mkfile(_)
    if _ not in ["-f", "-d"] and mode == "d":
        mkdir(_)
cdate = datetime.datetime.now()
str_to_file = cdate.strftime("%Y-%m-%d %H:%M:%S") + "\n"
while str_to_file != "stop\n":
    fil.write(str_to_file)
    str_to_file = str(input("Enter content line:")) + "\n"
