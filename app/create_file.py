from sys import argv
from os import makedirs, chdir
import os
import datetime


def create_path(list_of_args: list, index_d: int, index_f: int = None) -> None:
    if not index_f:
        index_f = len(list_of_args)
    cur_dir = os.getcwd()
    dir_path = os.path.join(cur_dir, *list_of_args[index_d + 1 : index_f])
    makedirs(dir_path)
    chdir(dir_path)


def make_file(file_name: str) -> None:
    with open(file_name, "a") as file1:
        file1.write("\n")
        line = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S")
        file1.write(f"{line}\n")
        row_number = 1
        line = input(
            "Enter content line: ",
        )
        while line != "stop":

            file1.write(f"{str(row_number)} {line}\n")
            line = input(
                "Enter content line: ",
            )
            row_number += 1


if ("-d" in argv) and ("-f" in argv):
    if argv.index("-d") < argv.index("-f"):
        create_path(argv, argv.index("-d"), argv.index("-f"))
    else:
        create_path(argv, argv.index("-d"))
    file_name = argv[argv.index("-f") + 1]
    make_file(file_name=file_name)
elif "-d" in argv:
    create_path(argv, argv.index("-d"))
elif "-f" in argv:
    file_name = argv[argv.index("-f") + 1]
    make_file(file_name=file_name)
