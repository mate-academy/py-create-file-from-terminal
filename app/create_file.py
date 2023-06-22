import os
from datetime import datetime
from argparse import ArgumentParser


def create_file(path: str) -> None:
    blank_line = ""
    if os.path.exists(path):
        blank_line = "\n"
    with open(path, "a") as file:
        if os.path.exists(path):
            file.write(blank_line)
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


path = ""
if args.d is not None:
    path = os.path.join(*args.d)
    if not os.path.exists(path):
        os.makedirs(path)
if args.f is not None:
    path = os.path.join(path, args.f)
    create_file(path)

