import datetime
import os
import sys


file_sys = sys.argv
date_now = datetime.datetime.now()
current_date = date_now.strftime("%Y-%m-%d %H:%M:%S")

if "-d" in file_sys and "-f" not in file_sys:
    directories = file_sys[file_sys.index("-d") + 1:]
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)

elif "-d" in file_sys and "-f" in file_sys:
    directories = file_sys[file_sys.index("-d") + 1:file_sys.index("-f")]
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)

if "-f" in file_sys:
    file_name = file_sys[file_sys.index("-f") + 1]

    with open(file_name, "a") as file:
        while True:
            file_line = input("Enter content line: ")
            if file_line == "stop":
                break
            file.write(f"{current_date}\n")
            file.write(f"{file_line}\n")
