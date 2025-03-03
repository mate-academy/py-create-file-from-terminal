from datetime import datetime
from os import makedirs
from sys import argv
import os
from typing import TextIO


def write_to_file(open_file_name: TextIO) -> None:
    open_file_name.write(datetime.now().strftime("%Y-%m-%d %I:%M:%S\n"))
    line_number = 1
    while True:
        input_line = input("Enter content line: ")
        if input_line == "stop":
            break
        open_file_name.write(str(line_number) + " " + input_line + "\n")
        line_number += 1


args = argv
if "-d" in args:
    if "-f" in args:
        file_name = args[-1]
        path = os.path.join(*args[args.index("-d") + 1:args.index("-f")])
        full_path = os.path.join(path, file_name)
    else:
        path = os.path.join(*args[args.index("-d") + 1:])
        full_path = path
if "-f" in args and "-d" not in args:
    file_name = args[-1]
    full_path = file_name

flags = {"-d": False, "-f": False}
if "-d" in args:
    flags["-d"] = True
if "-f" in args:
    flags["-f"] = True

if os.path.exists(full_path):
    with open(full_path, "a") as source_file:
        source_file.write("\n")
        write_to_file(source_file)
else:
    if flags["-d"] is True:
        makedirs(path)
    if flags["-f"] is True:
        with open(full_path, "w") as source_file:
            write_to_file(source_file)
