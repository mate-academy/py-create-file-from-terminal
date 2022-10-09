import sys
import os
from datetime import datetime


def create_file(file_name: str) -> None:
    if not os.path.isfile(file_name):
        mode = "w"
    else:
        mode = "a"
    with open(file_name, mode) as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time}\n")
        line_num = 1
        line = input("Enter content line: ")
        while line != "stop":
            f.write(f"{line_num} Line{line_num} {line}\n")
            line = input("Enter content line: ")
            line_num += 1


if ("-d" and "-f") in sys.argv:
    arg_d = sys.argv.index("-d")
    arg_f = sys.argv.index("-f")
    file_name = sys.argv[arg_f + 1]
    directory = sys.argv[arg_d + 1: arg_f]
    os.makedirs("/".join(directory))
    file_name_with_dir = "/".join(directory) + "/" + file_name
    create_file(file_name_with_dir)
elif "-f" in sys.argv:
    arg_f = sys.argv.index("-f")
    file_name = sys.argv[arg_f + 1]
    create_file(file_name)
elif "-d" in sys.argv:
    arg_d = sys.argv.index("-d")
    directory = sys.argv[arg_d + 1:]
    os.makedirs("/".join(directory))
