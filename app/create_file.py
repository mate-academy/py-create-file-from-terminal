import sys
import os
from datetime import datetime


def create_file() -> None:
    with open(sys.argv[-1], "a") as s:
        s.write(str(datetime.now().strftime("%m-%d-%Y %H:%M:%S")) + "\n")
        while True:
            new = input("Enter content line: ")
            if new == "stop":
                break
            s.write(new + "\n")
        s.write("\n")


def create_from_terminal():
    if "-d" in sys.argv and "-f" in sys.argv:
        os.makedirs("/".join(sys.argv[2:-2]))
        os.chdir(str("/".join(sys.argv[2:-2])))
        create_file()
    elif "-f" in sys.argv:
        create_file()
    elif "-d" in sys.argv:
        os.makedirs("/".join(sys.argv[-2:]))


create_from_terminal()
