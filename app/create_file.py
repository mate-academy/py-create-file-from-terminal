import sys
import os
from datetime import datetime


file_mode = False
file_info = []
folder_mode = False
folder_info = []
full_path = ""

for arg in sys.argv[1:]:
    if arg == "-f":
        file_mode = True
        folder_mode = False
        continue

    if arg == "-d":
        file_mode = False
        folder_mode = True
        continue

    if folder_mode:
        folder_info.append(arg)

    if file_mode:
        file_info.append(arg)

if len(file_info) > 0:
    file_mode = True

if len(folder_info) > 0:
    folder_mode = True

if folder_mode:
    full_path = os.path.join(os.getcwd(), *folder_info)
    os.makedirs(full_path)

if file_mode:
    for file_name in file_info:
        file_path = file_name

        if folder_mode:
            file_name = os.path.join(full_path, file_name)

        with open(file=file_name, mode="a") as file:
            stop = False
            current_date = str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
            file.write(f"{current_date}\r\n")
            current_line = 1
            while not stop:
                answer = input("Enter content line: ")
                if answer == "stop":
                    stop = True
                    continue
                file.write(f"{current_line} {answer}\r\n")
                current_line += 1
