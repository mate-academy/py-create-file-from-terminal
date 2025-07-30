import sys
import os
from datetime import datetime


def parse_args():
    args = sys.argv[1:]

    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        # zbieramy wszystko aż do następnej flagi lub końca listy
        next_flag = args[d_index + 1:]
        f_index = next_flag.index("-f") if "-f" in next_flag else len(next_flag)
        dir_path = os.path.join(*next_flag[:f_index])

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return dir_path, file_
