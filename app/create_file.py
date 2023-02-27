import os
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directories", type=str, nargs="+",
                    help="creating directories")
parser.add_argument("-f", "--file", type=str,
                    help="creating directories")
args = parser.parse_args()
print(args.__dict__)
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
    mode = "a" if os.path.exists(
        os.path.join(directory_path, file_name)
    ) else "w"

    with open(os.path.join(directory_path, file_name), mode) as file:
        if mode == "a":
            file.write("\n")

        file.write(f"{datetime.now().strftime('%Y-%m-%d %X')}\n")
        counter = 1

        lines = input("Enter content line: ")
        while lines != "stop":
            file.write(f"{counter} {lines}\n")
            lines = input("Enter content line: ")
            counter += 1
