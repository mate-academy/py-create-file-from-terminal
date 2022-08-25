from datetime import datetime
import os
import sys


def create_file():
    if "-d" in sys.argv:
        index = 2
        while index != len(sys.argv) and sys.argv[index] != "-f":
            os.mkdir(sys.argv[index])
            os.chdir(sys.argv[index])
            index += 1

    if "-f" in sys.argv:
        with open(sys.argv[-1], "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            line = 1
            while True:
                text = input("Enter content line: ")
                if text == "stop":
                    break
                file.write(f"{line} {text} \n")
                line += 1


create_file()
