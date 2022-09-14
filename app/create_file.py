import sys
import os
from datetime import datetime


def create_file(path_of_file):
    with open(path_of_file, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            data = input("Enter information: ")
            if data == "stop":
                break
            f.write(f"{data}\n")


if "-d" in sys.argv and "-f" not in sys.argv:
    args = sys.argv[2:]
    path_dir = os.path.join(*args)
    os.makedirs(path_dir)
if "-d" in sys.argv and "-f" in sys.argv:
    args = sys.argv[2:-2]
    path_dir = os.path.join(*args)
    os.makedirs(path_dir)
    path_file = path_dir + "/" + sys.argv[-1]
    create_file(path_file)
if "-d" not in sys.argv and "-f" in sys.argv:
    path_file = sys.argv[-1]
    create_file(path_file)
