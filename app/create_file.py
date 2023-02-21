import os
from datetime import datetime
from pathlib import Path
"""
create_file("python create_file.py -d dir1 dir2")
create_file("python create_file.py -f file.txt")
create_file("python create_file.py -d dir1 dir2 -f file.txt")

"""


def create_file(input_string: str) -> None:
    lg, f_name, flag, *destination_path = input_string.split()
    dir_path = [s for s in destination_path if s != "-f"]
    dirpath = os.path.join(*dir_path)
    output_file = Path(dirpath)
    if flag == "-d" and "-f" in destination_path:
        os.makedirs(os.path.dirname(dirpath), exist_ok=True)
        with open(output_file, "a") as target_file:
            write_content(target_file)
    elif flag == "-d":
        os.makedirs(dirpath, exist_ok=True)
    elif flag == "-f":
        with open(output_file, "a") as target_file:
            write_content(target_file)


def write_content(target_file: callable) -> None:
    ts = datetime.timestamp(datetime.now())
    ts = datetime.fromtimestamp(int(ts))
    target_file.write(str(ts) + "\n")
    number = 0
    while True:
        new_line = input("Enter content line:")
        if new_line == "stop":
            target_file.write("\n")
            break
        number += 1
        target_file.write("%d  %s" % (number, new_line + "\n"))
