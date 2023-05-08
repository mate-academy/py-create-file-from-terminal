import sys
import os
import datetime
import argparse


def create_new_path(new_path: list) -> str:
    path = os.getcwd()
    if new_path:
        path = os.path.join(path, *new_path)
        os.makedirs(path, exist_ok=True)
        return path


def create_and_write_to_file(new_path: list, file_name: list) -> None:
    now = datetime.datetime.now()
    input_text = now.strftime("%Y-%m-%d %H:%M:%S\n")
    while True:
        line = input()
        if line == "stop":
            break
        input_text += f"{line}\n"
    with open(
            os.path.join(create_new_path(new_path), *file_name),
            "a+"
    ) as target_file:
        target_file.write(f"{input_text}\n")


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file-name", nargs=1)
parser.add_argument("-d", "--new_path", nargs="*")
args = parser.parse_args()
argsdict = vars(args)

if "-d" in sys.argv:
    create_new_path(argsdict["new_path"])
if "-f" in sys.argv:
    create_and_write_to_file(argsdict["new_path"], argsdict["file_name"])
