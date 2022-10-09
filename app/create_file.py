from os import chdir, mkdir
from sys import argv
from datetime import datetime


def create_file() -> None:
    if "-d" in argv:
        i = 2

        while len(argv) != i:
            if argv[i] == "-f":
                i += 1
                continue

            mkdir(argv[i])
            chdir(argv[i])
            i += 1

    if "-f" in argv:
        with open(argv[-1], "w") as f:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{date}\n")

            current_line = 1
            inline_content = input("Enter content line: ")

            while inline_content != "stop":
                f.write(f"Line{current_line} {inline_content}\n")
                inline_content = input("Enter content line: ")
                current_line += 1


create_file()
