import argparse
import os
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument("-d", nargs='+', help="Enter the path", type=str)
parser.add_argument("-f", nargs='+', help="Enter the file name", type=str)
args = parser.parse_args()


def creating_directory(info):
    path_for_file = ""
    if info.d:
        d_path = "\\".join(info.d)
        path_for_directories = os.path.join(os.getcwd(), d_path)
        os.makedirs(path_for_directories)
        path_for_file += f"{'/'.join(info.d)}/"
    return path_for_file


def creating_a_new_file(info):
    if info.f:
        file_date = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        with open(f"{creating_directory(info)}{args.f[0]}", "a") as file:
            file.write(f"{file_date}\n")
            line_number = 1
            while True:
                line = input("Enter content line:")
                if line == "stop":
                    break
                file.write(f"{line_number} {line}\n")
                line_number += 1


creating_a_new_file(args)
