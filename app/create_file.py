import os
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs="*")
parser.add_argument("-f")
arguments = parser.parse_args()


def create_file(path: str) -> None:
    with open(path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        counter = 1
        while True:
            content = input()
            if content == "stop":
                f.write("\n")
                break
            f.write(f"{counter} {content}\n")
            counter += 1


if arguments.d and arguments.f:
    os.makedirs(os.path.join(*arguments.d), exist_ok=True)
    create_file(os.path.join(*arguments.d, arguments.d))

if arguments.d:
    os.makedirs(os.path.join(*arguments.f), exist_ok=True)

if arguments.f:
    create_file(arguments.f)
