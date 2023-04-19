import datetime
import os
import sys


args_from_terminal = sys.argv
if "-d" in args_from_terminal and "-f" in args_from_terminal:
    d_index = args_from_terminal.index("-d")
    f_index = args_from_terminal.index("-f")
    directories_path = "/".join(args_from_terminal[d_index + 1:f_index])
    file_name = args_from_terminal[-1]
    os.makedirs(directories_path)
    with open(
            os.path.join(
                directories_path,
                file_name
            ),
            "a"
    ) as file_to_create:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
        file_to_create.write(timestamp)
        line_number = 1
        line = input("Enter content line: ")
        while line != "stop":
            file_to_create.write(str(line_number) + " " + line + "\n")
            line = input("Enter content line: ")
            line_number += 1
elif "-f" not in args_from_terminal:
    d_index = args_from_terminal.index("-d")
    directories_path = "/".join(args_from_terminal[d_index + 1::])
    os.makedirs(directories_path)
elif "-d" not in args_from_terminal:
    file_name = args_from_terminal[-1]
    with open(file_name, "a") as file_to_create:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
        file_to_create.write(timestamp)
        line_number = 1
        line = input("Enter content line: ")
        while line != "stop":
            file_to_create.write(str(line_number) + " " + line + "\n")
            line = input("Enter content line: ")
            line_number += 1
