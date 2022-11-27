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


def create_from_terminal() -> None:

    if sys.argv[1] == "-d":
        path = os.path.join(sys.argv[2], sys.argv[3])
        os.makedirs(path)
        if "-d" in sys.argv and "-f" in sys.argv:
            os.chdir(path)
            create_file()
    else:
        create_file()


create_from_terminal()
