import sys
import os
from datetime import datetime

commands_list = sys.argv[1:]

dirs = []
user_file = commands_list[commands_list.index("-f") + 1:][0]

if "-d" in commands_list:
    for el in commands_list[1:]:
        if el == "-f":
            break
        dirs.append(el)

path_for_file = os.path.join(*dirs)

if os.path.isdir(path_for_file):
    is_file_exist = True
else:
    is_file_exist = False
    os.makedirs(path_for_file)

with open(os.path.join(*dirs, user_file), "a") as a:
    if not is_file_exist:
        a.write(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
    user_data_line = input("Enter content line: ")

    while user_data_line.lower() != "stop":
        a.write(f"{user_data_line}\n")
        user_data_line = input("Enter content line: ")
