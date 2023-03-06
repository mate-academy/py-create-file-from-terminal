import os
import argparse
from datetime import datetime


parser = argparse.ArgumentParser(description="parsing command from terminal")
parser.add_argument("-d", "--directories", type=str, nargs="+",
                    help="creating directories")
parser.add_argument("-f", "--file", type=str,
                    help="creating directories")
args = parser.parse_args()

temp = ""
if args.__dict__["directories"] is not None:

    for directory in args.__dict__["directories"]:
        temp = os.path.join(temp, directory)
        if not os.path.exists(temp):
            os.mkdir(temp)


if args.__dict__["file"] is not None:
    directory_path = os.getcwd()
    if os.path.exists(temp):
        directory_path = temp
    file_name = args.__dict__["file"]

    with open(os.path.join(directory_path, file_name), "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %X')}\n")
        counter = 1

        lines = input("Enter content line: ")
        while True:
            if lines != "stop":
                file.write(f"{counter} {lines}\n")
                lines = input("Enter content line: ")
                counter += 1
            else:
                file.write("\n")
                break
