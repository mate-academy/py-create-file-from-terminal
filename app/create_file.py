import sys
import os
from datetime import datetime


file_mode = False
file_info = ""
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
        print(f"folder_info += {arg}")
        folder_info.append(arg)

    if file_mode:
        print(f"file_info = {arg}")
        file_info = arg

if len(file_info) > 0:
    file_mode = True

if len(folder_info) > 0:
    folder_mode = True

if folder_mode:
    full_path = os.path.join(os.getcwd(), "\\".join(folder_info))
    os.makedirs(full_path)

if file_mode:
    if folder_mode:
        os.chdir(full_path)

    with open(file=file_info, mode="a") as file:
        stop = False
        current_date = str(datetime.now())[:19]
        file.write(f"{current_date}\r\n")
        while not stop:
            answer = input("Enter content line: ")
            if answer == "stop":
                stop = True
                continue
            file.write(f"{answer}\r\n")
