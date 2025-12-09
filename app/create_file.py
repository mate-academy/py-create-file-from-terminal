import os
import sys
import datetime
from typing import TextIO

terminal = sys.argv
if "-d" not in terminal and "-f" not in terminal:
    sys.exit("No terminal provided")

def write(open_file: TextIO) -> None:
    input_user = None
    line = 1
    open_file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S \n"))
    while input_user != "stop\n":
        input_user = input("Enter content line: ")
        input_user = f"{line} {input_user}\n"

        open_file.write(input_user if input_user != f"{line} stop\n" else "")

        input_user = input_user.strip(f"{line} ")
        line += 1


def creating_a_directory(name_directory: list) -> None:
    path = os.path.join(*name_directory)
    os.makedirs(path, exist_ok=True)


def creating_a_file(filename: str) -> None:
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            data = file.read()
        with open(filename, "w") as file:
            file.write(f"{data}\n")
            write(file)
    else:
        with open(filename, "w") as file:
            write(file)


def creating_a_file_in_a_directory(director: list[str],
                                   path_to_file: str) -> None:
    creating_a_directory(director)
    creating_a_file(path_to_file)


if "-d" in terminal and "-f" in terminal:
    patch = os.path.join(*terminal[1 + terminal.index("-d"):
                                   terminal.index("-f")],
                         terminal[1 + terminal.index("-f")])
    directory = terminal[1 + terminal.index("-d"):terminal.index("-f")]
    creating_a_file_in_a_directory(directory, patch)

elif "-d" in terminal:
    creating_a_directory(terminal[2:])

elif "-f" in terminal:
    creating_a_file(terminal[2])
