import sys
import os
from datetime import datetime


def parse_args() -> tuple[str, str]:
    args = sys.argv[1:]
    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        next_flag = args[d_index + 1:]
        if "-f" in next_flag:
            f_index = next_flag.index("-f")
        else:
            f_index = len(next_flag)
        path_parts = next_flag[:f_index]
        dir_path = os.path.join(*path_parts)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    return dir_path, file_name


def collect_content() -> list[s]()_
