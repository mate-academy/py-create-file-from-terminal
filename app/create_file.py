import os
import sys
import datetime


def create_file():
    if "-d" in sys.argv:
        count = 2
        while len(sys.argv) != count and sys.argv[count] != "-f":
            os.mkdir(sys.argv[count])
            os.chdir(sys.argv[count])
            count += 1
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
