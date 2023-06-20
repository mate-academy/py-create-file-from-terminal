import sys
import os
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    if directory:
        if not os.path.exists(directory):
            os.makedirs(directory)
        path = os.path.join(directory, filename)
    counter = 1
    if filename:
        with open(f"{path}.txt", "a") as new_file:
            new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            new_line = input("Enter content line: ")
            while new_line != "stop":
                new_file.write(f"{counter} {new_line}\n")
                counter += 1
                new_line = input("Enter content line: ")


def main() -> None:
    directory = ""
    filename = ""
    if "-d" in sys.argv:
        directory = "/".join(sys.argv[sys.argv.index("-d") + 1:])
    if "-f" in sys.argv:
        filename = sys.argv[sys.argv.index("-f") + 1:]
    if directory and filename:
        directory = ("/".join(sys.argv[sys.argv.index("-d")
                                       + 1:sys.argv.index("-f") - 1]))
        create_file(directory, filename)
    create_file(directory, filename)
