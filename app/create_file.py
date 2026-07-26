import os
import sys
from datetime import datetime


TODAY = datetime.now()
DAT_LIST = str(TODAY).split(".")
DAT = DAT_LIST[0]
TERMINAL_STR = " ".join(sys.argv)


def creater():
    with open("file.txt", "a") as file:
        file.write(DAT + "\n")
        print(os.getcwd())
        for line in sys.stdin:
            print(f"Enter content line: {line}")
            d = line.replace("stop", "")
            file.write(d)
            if "stop" == line.rstrip():
                break


if "-d" in sys.argv and "-f" not in sys.argv:
    TERMINAL_D = TERMINAL_STR.partition("-d ")[2]
    TERMINAL_D_ = str(TERMINAL_D.replace(" ", "/"))
    os.makedirs(TERMINAL_D_)

if "-f" in sys.argv and "-d" not in sys.argv:
    creater()

if "-d" in sys.argv and "-f" in sys.argv:
    TERMINAL_DF = TERMINAL_STR.partition("-d ")[2]
    TERMINAL_DF = TERMINAL_DF.partition(" -f")[0]
    TERMINAL_DF_ = TERMINAL_DF.replace(" ", "/")
    os.makedirs(TERMINAL_DF_)
    os.chdir(TERMINAL_DF_)
    creater()
