import sys
import os
from datetime import datetime


def get_path_from_args() -> str:
    result_path = ""
    if sys.argv.count("-d") > 1:
        raise ValueError("-d flag is already defined")
    elif sys.argv.count("-f") > 1:
        raise ValueError("-f flag is already defined")

    if "-d" in sys.argv:
        flag_idx = sys.argv.index("-d")
        if len(sys.argv) < flag_idx + 2:
            raise ValueError("-d flag requires two parameters")
        result_path = os.path.join(sys.argv[flag_idx + 1],
                                   sys.argv[flag_idx + 2])
        os.makedirs(result_path)
    if "-f" in sys.argv:
        flag_idx = sys.argv.index("-f")
        if len(sys.argv) < flag_idx + 1:
            raise ValueError("-f flag requires one parameter")
        result_path = os.path.join(result_path, sys.argv[flag_idx + 1])
    else:
        raise ValueError("There is not -f flag")
    return result_path


# get information from console args
path = get_path_from_args()


# Write file content
with open(path, "w") as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    line_counter = 1
    data = ""
    while True:
        data = input("Enter content line: ")
        if data == "stop":
            break
        f.write(f"{line_counter} {data}\n")
        line_counter += 1
