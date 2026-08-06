import os
import sys
from datetime import datetime


args = sys.argv[1:]
dirs = []
file_name = None

if "-d" in args:
    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")
        if f_index > d_index:
            dirs = args[d_index + 1: f_index]
        else:
            dirs = args[d_index + 1:]
    else:
        dirs = args[d_index + 1:]

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

path = ""
if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

file_path = None
if file_name:
    if dirs:
        file_path = os.path.join(path, file_name)
    else:
        file_path = file_name

if file_name:
    file_exists = os.path.exists(file_path)
    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            else:
                file.write(f"{line_number} {user_input}\n")
                line_number += 1
