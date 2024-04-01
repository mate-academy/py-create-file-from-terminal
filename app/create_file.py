import argparse
import sys
import os
import datetime


def write_info(file_name: str) -> None:

    line = input("Enter content line: ")
    with open(file_name, "a") as file_open:
        if os.stat(file_name).st_size:
            file_open.write("\n")

        counts = 1
        while line != "stop":
            if counts == 1:
                file_open.write(datetime.datetime.now()
                                .strftime("%Y-%m-%d %H:%M:%S")
                                + "\n")
            file_open.write(f"{counts} {line}\n")
            line = input("Enter content line: ")
            counts += 1


new_path = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument("-f", nargs=1, dest="file_work", required=True,
                    help="Only 1 name of file to write")
parser.add_argument("-d", nargs="*", dest="dicts", default=None)
parser.add_argument("baz", nargs="*")
argss = parser.parse_args(sys.argv)

if argss.dicts:
    new_path = os.path.join(new_path, os.path.sep.join(argss.dicts))
os.makedirs(new_path, exist_ok=True)
write_info(os.path.join(new_path, argss.file_work[0]))
