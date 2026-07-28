import sys
import os
from datetime import datetime


command = sys.argv

file_name = None
directories = []

if "-f" in command:
    f_index = command.index("-f")
    if f_index + 1 < len(command):
        file_name = command[f_index + 1]

if "-d" in command:
    d_index = command.index("-d")

    if "-f" in command:
        f_index = command.index("-f")
        if d_index < f_index:
            directories = command[d_index + 1:f_index]
        else:
            directories = command[d_index + 1:]
    else:
        directories = command[d_index + 1:]


if directories:
    path = "/".join(directories)
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

if file_name:
    if directories:
        file_path = path + "/" + file_name
    else:
        file_path = file_name

    list_file = []

    while True:
        enter = input("Enter content line: ")
        if enter == "stop":
            break
        list_file.append(enter)

    file_existed = os.path.exists(file_path)
    with open(file_path, "a") as file:
        if file_existed:
            file.write("\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        for index, line in enumerate(list_file, start=1):
            file.write(f"{index} {line}\n")
