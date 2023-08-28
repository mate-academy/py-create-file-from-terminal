import sys
import os
from datetime import datetime


def create_dir() -> None:
    if "-f" in sys.argv:
        if sys.argv.index("-f") > sys.argv.index("-d"):
            dir_path = os.path.join(*sys.argv[2:-2])
        else:
            dir_path = os.path.join(*sys.argv[sys.argv.index("-d") + 1:])
    else:
        dir_path = os.path.join(*sys.argv[2:])
    os.makedirs(dir_path, exist_ok=True)


def create_file() -> None:
    if "-d" in sys.argv:
        if sys.argv.index("-f") > sys.argv.index("-d"):
            file_path = os.path.join(*sys.argv[2:-2], sys.argv[-1])
        else:
            file_path = os.path.join(
                *sys.argv[sys.argv.index("-d") + 1:],
                sys.argv[sys.argv.index("-f") + 1:sys.argv.index("-d")][0])
    else:
        file_path = sys.argv[2]

    with open(file_path, "a") as file:
        text = str(datetime.today().strftime("%Y-%m-%d %H:%M:%S"))
        file.write(text + "\n")

        while text != "stop":
            text = input("Enter content line: ")
            if text != "stop":
                file.write(text + "\n")
        file.write("\n")


if "-d" in sys.argv:

    create_dir()

if "-f" in sys.argv:

    create_file()
