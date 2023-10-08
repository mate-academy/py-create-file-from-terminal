import datetime
import os
import sys


def create_file(path: str) -> None:
    with open(path, "a") as file:
        file.write(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                   + "\n")
        line = input("Enter content line: ")
        index = 1
        while line != "stop":
            file.write(f"{index} {line}\n")
            index += 1
            line = input("Enter content line: ")
        file.write("\n")


def read_line() -> None:
    line_args = sys.argv
    index = 1
    while index < len(line_args):
        if line_args[index] == "-d":
            os.makedirs(os.path.join("app", line_args[index + 1]))
            os.makedirs(os.path.join("app", line_args[index + 2]))
            index += 3
        elif line_args[index] == "-f":
            create_file(os.path.join("app", line_args[index + 1]))
            index += 2


read_line()
