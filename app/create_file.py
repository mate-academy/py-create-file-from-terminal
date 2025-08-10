import sys
import os
import datetime


def create_file():
    if "-d" in sys.argv:
        index = 2
        while len(sys.argv) != index and sys.argv[index] != "-f":
            os.mkdir(sys.argv[index])
            os.chdir(sys.argv[index])
            index += 1
    if "-f" in sys.argv:
        with open(sys.argv[-1], "w") as file:
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{time}\n")
            line = 1
            new_line = input("Enter content line: ")
            while new_line != "stop":
                file.write("Line" + f"{line}" + f"{new_line}")
                new_line = input("Enter content line: ")
                line += 1
