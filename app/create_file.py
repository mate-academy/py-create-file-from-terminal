import sys
import os
from datetime import datetime


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_name):
    with open(file_name, "a") as f:
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(date_time)
        i = 0
        line = ""
        while line != "stop":
            f.write(f"{i} {line} \n")
            i += 1
            line = input("Enter content line: ")


def create_directory_and_file():
    if "-d" in sys.argv and "-f" in sys.argv:
        path = ""
        for directory in sys.argv[sys.argv.index("-d") + 1: len(sys.argv) - 2]:
            path += f"{directory}/"
        create_directory(path)
        create_file(f"{path}/{sys.argv[-1]}")

    elif "-d" in sys.argv and "-f" not in sys.argv:
        path = ""
        for directory in sys.argv[sys.argv.index("-d") + 1: len(sys.argv) - 2]:
            path += f"{directory}/"
        create_directory(path)

    elif "-f" in sys.argv and "-d" not in sys.argv:
        create_file(sys.argv[-1])


create_directory_and_file()
