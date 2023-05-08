import sys
import os
import datetime
import argparse


def create_new_path(new_path: list) -> str:
    path = os.getcwd()
    for folder in new_path:
        path = os.path.join(path, folder)
    if os.path.exists(path):
        return path
    os.makedirs(path)


def create_and_write_to_file(new_path: list, file_name: list) -> None:
    now = datetime.datetime.now()
    input_text = now.strftime("%Y-%m-%d %H:%M:%S\n")
    while True:
        line = input()
        if line == "stop":
            with open(
                    os.path.join(create_new_path(new_path), file_name[0]),
                    "a+"
            ) as target_file:
                target_file.write(f"{input_text}\n")
                break
        input_text += f"{line}\n"


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file-name", nargs="*")
parser.add_argument("-d", "--new_path", nargs="*")
args = parser.parse_args()
argsdict = vars(args)

if "-f" in sys.argv:
    create_new_path(argsdict["new_path"])
if "-d" in sys.argv:
    create_and_write_to_file(argsdict["new_path"], argsdict["file_name"])
