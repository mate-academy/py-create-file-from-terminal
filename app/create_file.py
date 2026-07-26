import os
import sys
from datetime import datetime


def write_to_file_by_console(path: str) -> None:
    with open(path, "a") as file:
        file.write(datetime.now().strftime("%y-%m-%d %H:%M:%S\n"))
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(line + "\n")


def write_to_file(path: str, text: str) -> None:
    with open(path, "a") as file:
        file.write(text)


args = sys.argv[1:]

if "-d" not in args:
    if "-f" in args:
        filename = args[args.index("-f") + 1]
        write_to_file_by_console(filename)
else:
    d_index = args.index("-d") + 1

    if "-f" in args:
        f_index = args.index("-f")
        filename = args[f_index + 1]

        path = os.path.join(*args[d_index:f_index], filename)

        if os.path.exists(path):
            write_to_file(path, "\n")
        else:
            os.makedirs(os.path.join(*args[d_index:f_index]))

        write_to_file_by_console(path)
    else:
        os.makedirs(os.path.join(*args[d_index:]))
