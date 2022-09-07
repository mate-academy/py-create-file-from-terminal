import os
import sys
from datetime import datetime


def create_dir(path_list):
    # create a path to a directory and actually directories
    path = "/".join(path_list)
    os.makedirs(path, exist_ok=True)


def create_file(path_file):
    # create a path to a file
    if isinstance(path_file, list):
        path = "/".join(path_file)
    else:
        path = path_file
    # write file with appropriate time
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as f:
        f.write(f"{time}\n")
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                f.write("\n")
                break
            f.write(f"{content}\n")


def read_pass():
    terminal_line = sys.argv
    # split terminal line into pieces to understand purpose of message
    # create directories and file
    if "-f" in terminal_line and "-d" in terminal_line:
        index_d = terminal_line.index("-d")
        index_f = terminal_line.index("-f")
        create_dir(terminal_line[index_d + 1: index_f])
        file = terminal_line[index_d + 1: index_f] + \
            terminal_line[index_f + 1:]
        create_file(file)
    # create directories
    elif '-d' in terminal_line:
        index_d = terminal_line.index("-d")
        create_dir(terminal_line[index_d + 1:])
    # create file into current directory
    elif "-f" in terminal_line:
        index_f = terminal_line.index("-f")
        create_file(terminal_line[index_f + 1:])


read_pass()
