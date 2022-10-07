import os
import sys
from datetime import datetime


def create_file():
    if "-d" in sys.argv:
        i = 2
        while i < len(sys.argv) and sys.argv[i] != "-f":
            os.mkdir(sys.argv[i])
            os.chdir(sys.argv[i])
            i += 1

    if "-f" in sys.argv:
        with open(sys.argv[-1], "a") as file:
            now = datetime.now()
            file.write(f"{now.strftime('%m/%d/%Y, %H:%M:%S')}")

            new_line = input("Enter a new line or 'stop' to exit: ")

            line_count = 1

            while new_line != "stop":
                file.write(f"{line_count} {new_line}\n")
                line_count += 1
                new_line = input("Enter a new line or 'stop' to exit: ")


create_file()
