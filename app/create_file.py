import sys
import os
from datetime import datetime
from argparse import ArgumentParser


def create_file(path: str) -> None:
    path = os.path.join(path, args.f)

    with open(path, "a") as file:
        if os.path.exists(path):
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                break
            file.write(f"{input_line}\n")


parser = ArgumentParser()

parser.add_argument("-d", nargs="*")
parser.add_argument("-f")

args = parser.parse_args()

if "-d" in sys.argv:
    if "-f" in sys.argv:
        path = os.path.join(*args.d)
        os.makedirs(path, exist_ok=True)
        create_file(path)
    else:
        path = os.path.join(*args.d)
        os.makedirs(path)
elif "-f" in sys.argv:
    create_file("")
