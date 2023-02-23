import os
from datetime import datetime
from pathlib import Path
"""
create_file("python create_file.py -d dir1 dir2")
create_file("python create_file.py -f file.txt")
create_file("python create_file.py -d dir1 dir2 -f file.txt")
create_file("python create_file.py -f file.txt -d dir1 dir2")
"""


def check_str(input_string: str) -> tuple:
    str_ = input_string.split()
    unused1, unused2, flag, *path_ = str_
    if flag == "-d":
        if "-f" in path_:
            if str_.index("-d") < str_.index("-f"):
                dr, filename = path_[0:-2], path_[-1]
                return dr, filename
        dr = path_[0:]
        return dr, []
    elif flag == "-f":
        if "-d" in path_:
            if str_.index("-f") < str_.index("-d"):
                dr, filename = path_[2:], path_[0]
                return dr, filename
        filename = path_[-1]
        return [], filename


def create_file(path_: str) -> None:
    dr, filename = check_str(path_)
    if not dr:
        write_content(filename)
    elif not filename:
        dirpath = os.path.join(*dr)
        os.makedirs(dirpath, exist_ok=True)
    elif dr and filename:
        pat = dr + [filename]
        dirpath = os.path.join(*pat)
        Path(dirpath).parent.mkdir(exist_ok=True, parents=True)
        write_content(dirpath)


def write_content(_file: str) -> None:
    with open(_file, "a") as target_file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        target_file.write(current_time + "\n")
        number = 0
        while True:
            new_line = input("Enter content line:")
            if new_line == "stop":
                target_file.write("\n")
                break
            number += 1
            target_file.write("%d  %s" % (number, new_line + "\n"))
