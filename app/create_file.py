import datetime
import os
import sys


def create_full_path(path, name):
    create_dirs(path)

    with open(path + os.path.sep + name, "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        count = 1
        while True:
            input_string = input("Enter content line: ")
            if input_string == "stop":
                f.write("\n")
                break
            f.write(f"{count} {input_string}\n")
            count += 1


def create_dirs(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def create_file():
    if "-d" in sys.argv and "-f" in sys.argv:
        create_full_path(os.path.sep.join(
            sys.argv[sys.argv.index("-d") + 1:sys.argv.index("-f")]),
            sys.argv[-1])
    elif "-d" in sys.argv:
        create_dirs(os.path.sep.join(sys.argv[sys.argv.index("-d") + 1:]))
    elif "-f" in sys.argv:
        create_full_path(os.path.curdir, sys.argv[-1])
