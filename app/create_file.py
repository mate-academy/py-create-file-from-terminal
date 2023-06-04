import sys
from sys import argv
import os
from datetime import datetime

argv = argv[1:]
if "-f" in argv:
    try:
        file_name = argv[argv.index("-f") + 1]
    except IndexError:
        print("Invalid data has inputed")
        sys.exit(1)
    if "-d" in argv:
        try:
            dir_list = (argv[argv.index("-d") + 1: argv.index("-f")]
                        or argv[argv.index("-d") + 1: len(argv)])
            path = os.path.join(*dir_list)
            os.makedirs(path, exist_ok=True)
        except Exception as e:
            print(e)
            sys.exit(1)
        file_name = os.path.join(path, file_name)

        with open(file_name, "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            line_number = 1
            while True:
                inputed_line = input("Enter content line: ")
                if inputed_line.lower() == "stop":
                    file.write("\n")
                    break
                file.write(f"{line_number} {inputed_line}\n")
                line_number += 1
elif "-d" in argv:
    try:
        path = os.path.join(*[argv[i] for i in range(1, len(argv))])
        os.makedirs(path, exist_ok=True)
    except TypeError:
        print("Missing directory name")
