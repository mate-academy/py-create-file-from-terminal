from sys import argv
import os
from datetime import datetime


f_appeared = False
d_appeared = False
i = 1
while i < len(argv):
    if argv[i] == "-f":
        f_appeared = True
        file_path = argv[i + 1]
        i += 2
    else:
        d_appeared = True
        j = i + 1
        while j < len(argv) and argv[j] != "-f":
            j += 1
        folders = os.path.join(*argv[i + 1:j])
        i = j
if d_appeared:
    os.makedirs(folders, exist_ok=True)
if f_appeared:
    if d_appeared:
        file_path = os.path.join(folders, file_path)
    file_existed = os.path.isfile(file_path)
    with open(file_path, "a") as file:
        if file_existed:
            print(file=file)
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), file=file)
        i = 1
        row = input("Enter content line: ")
        while row != "stop":
            print(i, row, file=file)
            i += 1
            row = input("Enter content line: ")