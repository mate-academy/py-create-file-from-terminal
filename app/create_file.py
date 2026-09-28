import os
import datetime
import sys
from enum import Enum


class ArgMode(Enum):
    NONE = "None"
    DIRECTORY = "directory"
    FILE = "file"


def create_file(*args) -> None:
    curr_path = ""
    file_name = ""
    curr_switch = ArgMode.NONE
    for arg in args:
        if arg == "-d":
            curr_switch = ArgMode.DIRECTORY
        elif arg == "-f":
            curr_switch = ArgMode.FILE

        elif curr_switch == ArgMode.DIRECTORY:
            curr_path += arg if curr_path == "" else "/" + arg
        elif curr_switch == ArgMode.FILE:
            file_name = arg

    if curr_path != "":
        os.makedirs(curr_path, exist_ok=True)
        curr_path += "/"

    if file_name != "":
        curr_path += file_name

        open_method = "w"
        if os.path.exists(curr_path):
            open_method = "a"

        with open(curr_path, open_method) as file:
            if open_method == "a":
                file.write("\n")

            file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

            count = 0
            while True:
                new_line = input("Enter content line: ")
                if new_line == "stop":
                    break
                count += 1
                file.write(f"{count} {new_line}\n")


create_file(*sys.argv[1:])
