from os import path, makedirs
from sys import argv
from datetime import datetime


""" Checking flags block """

dir_arg, file_arg = False, False
dir_path, file_name = "", ""
for argument in argv:
    if argument == "-d" and not dir_path:
        dir_arg = True
        file_arg = False
        continue
    if argument == "-f":
        if not file_name:
            file_arg = True
        dir_arg = False
        continue

    if dir_arg:
        dir_path = path.join(dir_path, argument)

    if file_arg:
        ext = ""
        ext_1 = path.splitext(argument)[-1]
        if ext_1 != ".txt":
            ext = ".txt"
        file_name = argument + ext
        file_arg = False

""" Creating directory block """

if dir_path:
    if not path.exists(dir_path):
        makedirs(dir_path)

""" Creating file block"""

if file_name:
    if dir_path:
        file_name = path.join(dir_path, file_name)

    lines = [datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")]
    line = ""
    line_counter = 0
    print("Enter file content (type \'stop\' to end the file):")
    while line != "stop":
        line_counter += 1
        line = input("Enter content line: ")
        lines.append(f"{line_counter} {line}") if line != "stop" else None
    with open(file_name, "w") as text_file:
        for line in lines:
            text_file.write(f"{line}\n")
