import sys
import os
from datetime import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file_out:
        file_out.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_num = 1
        line = input("Enter content line: ")
        while line != "stop":
            file_out.write(f"{line_num} {line}\n")
            line = input("Enter content line: ")
            line_num += 1
        file_out.write("\n")


if "-d" in sys.argv and "-f" in sys.argv:
    arg_d = sys.argv.index("-d")
    arg_f = sys.argv.index("-f")
    file_name = sys.argv[arg_f + 1]
    directory = "/".join(sys.argv[arg_d + 1: arg_f])
    if not os.path.isdir(directory):
        os.makedirs(directory)
    file_name_with_dir = directory + "/" + file_name
    create_file(file_name_with_dir)

elif "-f" in sys.argv:
    arg_f = sys.argv.index("-f")
    file_name = sys.argv[arg_f + 1]
    create_file(file_name)

elif "-d" in sys.argv:
    arg_d = sys.argv.index("-d")
    directory = sys.argv[arg_d + 1:]
    os.makedirs("/".join(directory))
