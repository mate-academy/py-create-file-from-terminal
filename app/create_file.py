import os
import sys

from datetime import datetime as datetime


def create() -> None:
    args = sys.argv[1::]
    path = os.getcwd

    if "-d" in args:
        if args[-2] == "-f":
            path = os.path.join(*args[1:-2], "")
        else:
            path = os.path.join(*args[1::], "")
        os.makedirs(path)

    if "-f" in args:
        with open(os.path.join(path, args[args.index("-f") + 1]), "a") as f:
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n")
            line_number = 1
            while True:
                input_line = input("Enter content line: ")
                if input_line == "stop":
                    break
                f.write(f"{line_number} {input_line} \n")
                line_number += 1
