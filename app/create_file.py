import datetime
import os
import sys
from copy import deepcopy
from os.path import isdir


def create_file_inner(*argt) -> None:

    args = argt[0]
    args_len = len(args)
    if args_len < 2:
        print("Too few arguments (must be at least 2)")
        return

    if not ("-d" in args or "-f" in args):
        print("-d of -f should be present")
        return

    if "-f" in args:
        f_position = args.index("-f")
    else:
        f_position = -1

    if "-d" in args:
        d_position = args.index("-d")
    else:
        d_position = -1

    if (f_position > -1
            and d_position > -1
            and abs(f_position - d_position) == 1):
        print("-d and -f are present but info is missed")
        return

    file_name = get_file_name(args, f_position)
    if file_name is None:
        print("-f flag is present but file name missed")

    dir_info = get_dir_info(args, d_position, f_position)
    one_path = ""
    for one_dir in dir_info:
        one_path = os.path.join(one_path, one_dir)
        if not isdir(one_path):
            os.mkdir(one_path)

    if f_position >= 0:
        file_path = os.path.join(one_path, file_name)
        date_time_info = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        with open(file_path, "a") as target_file:
            target_file.write(date_time_info + "\n")
            for line in args[args_len - 1]:
                target_file.write(line + "\n")
            target_file.write("\n")
    return


def get_file_name(args: tuple, f_position: str) -> str:
    try:
        return args[f_position + 1]
    except IndexError:
        print("-f flag is present but file name missed")
        return None


def get_dir_info(args: tuple, d_position: str, f_position: str) -> list:
    result = []
    if d_position < 0:
        return result
    args_len = len(args)
    while True:
        result.append(args[d_position + 1])
        if d_position == args_len - 3 or d_position == f_position - 2:
            return result
        d_position += 1


arguments = deepcopy(sys.argv)
arguments.pop(0)

lines = []
while True:
    line = input("Enter contain line: ")
    if line == "stop":
        break
    lines.append(line)
arguments.append(lines)
create_file_inner(arguments)
