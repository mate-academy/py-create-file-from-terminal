import sys
import os
from datetime import datetime


def create_file():
    if "-d" in sys.argv and "-f" not in sys.argv:
        path = os.path.join(*sys.argv[2:])
        if not os.path.exists(path):
            os.makedirs(path)
            return

    path = ""
    if "-d" in sys.argv and "-f" in sys.argv:
        path = os.path.join(*sys.argv[2:-2])
        if not os.path.exists(path):
            os.makedirs(path)

    with open(f"{os.path.join(path, sys.argv[-1])}", "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break

            file.write(f"{line}\n")


if __name__ == '__main__':
    create_file()
