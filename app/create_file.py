import datetime
import os
import sys


def file_create():
    if '-d' in sys.argv:
        index = 2
        while index != len(sys.argv) and sys.argv[index] != "-f":
            os.mkdir(sys.argv[index])
            os.chdir(sys.argv[index])
            index += 1

    if '-f' in sys.argv:
        with open(sys.argv[-1], "a") as file:
            current = datetime.datetime.now()
            file.write(f"{current.strftime('%Y-%m-%d %H:%M:%S')}\n")
            next_line = input("Enter content line: ")
            count_lines = 1
            while next_line != "stop":
                file.write(f"{count_lines} {next_line}\n")
                next_line = input("Enter content line: ")
                count_lines += 1
            file.write("\n")


file_create()
