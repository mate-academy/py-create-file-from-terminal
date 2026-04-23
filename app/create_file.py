import os
import sys
from datetime import datetime


console_data = sys.argv

if "-d" in console_data:
    parent_dir = console_data[console_data.index("-d") + 1]
    path = os.path.join(parent_dir, console_data[console_data.index("-d") + 2])
    os.makedirs(path)

if "-f" in console_data:

    if "-d" in console_data:
        parent_dir = console_data[console_data.index("-d") + 1]
        new_dir = console_data[console_data.index("-d") + 2]
        file_name = console_data[console_data.index("-f") + 1]
        file_path = os.path.join(parent_dir, new_dir, file_name)
    else:
        file_path = console_data[console_data.index("-f") + 1]

    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        counter = 0

        while True:
            message = input("Enter content line: ")
            counter += 1
            if message == "stop":
                break
            file.write(f"{counter} {message}\n")
