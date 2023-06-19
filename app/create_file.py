import sys
import os
from datetime import datetime


def create_file(path: str) -> None:
    path = os.path.join(path, sys.argv[sys.argv.index("-f") + 1])

    mode = "w"
    if os.path.exists(path):
        mode = "a"

    with open(path, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                break
            else:
                file.write(f"{input_line}\n")


if "-d" in sys.argv:
    if "-f" in sys.argv:
        path = os.path.join(*sys.argv[sys.argv.index("-d")
                                      + 1:sys.argv.index("-f")])
        if not os.path.exists(path):
            os.makedirs(path)
        create_file(path)
    else:
        path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
        os.makedirs(path)
elif "-f" in sys.argv:
    create_file("")
