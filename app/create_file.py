import sys
import os
from datetime import datetime


arg = sys.argv


def make_dir(dirs: list):
    path_dir = "/".join(dirs)
    os.makedirs(path_dir)


def work_with_file(file: str):
    list_of_line = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        list_of_line.append(line)

    with open(file, "a") as f:
        now = datetime.now()
        f.write(now.strftime("%Y %m %d %H %M %S"))
        count_lines = 1
        for line in list_of_line:
            f.write(str(count_lines) + " " + line + "\n")
            count_lines += 1


def create_file(args: list):
    if args[1] == "-d":
        path = args[2:]
        make_dir(path)
    if args[1] == "-f":
        file_name = args[-1]
        work_with_file(file_name)
    if args[1] == "-d" and args[2] == "-f":
        dir_path = args[2:4]
        file_path = "/".join(args[2:4]) + "/" + args[-1]
        make_dir(dir_path)
        work_with_file(file_path)
