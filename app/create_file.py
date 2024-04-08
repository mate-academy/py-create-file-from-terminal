import argparse
import sys
import os
import datetime


def write_info(file_name: str) -> None:

    line = input("Enter content line: ")
    counts = 1
    string_to_file = ""
    while line != "stop":
        if counts == 1:
            string_to_file = (
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                + "\n"
            )
        string_to_file += f"{counts} {line}\n"
        line = input("Enter content line: ")
        counts += 1

    with open(file_name, "a") as file_open:
        if os.stat(file_name).st_size:
            string_to_file = "\n" + string_to_file
        file_open.write(string_to_file)


new_path = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("-f", nargs=1, dest="file_work", required=True,
                    help="Only 1 name of file to write")
parser.add_argument("-d", nargs="*", dest="dicts", default=None)
parser.add_argument("pos_args", nargs="*")
argss = parser.parse_args(sys.argv)

if argss.dicts:
    new_path = os.path.join(new_path, os.path.sep.join(argss.dicts))

    for char in '|*?"</>':
        if char in new_path:
            raise OSError(f"Wrong char {char} in command dir")

for char in ':|*?"</>':
    if char in argss.file_work[0]:
        raise OSError(f"Wrong char {char} in file")

os.makedirs(new_path, exist_ok=True)
write_info(os.path.join(new_path, argss.file_work[0]))
