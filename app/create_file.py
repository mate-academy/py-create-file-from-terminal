import datetime
import os
import sys

args = sys.argv
date_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dir_path = "."
file_name = None
if "-d" in args:
    dir_index = args.index("-d") + 1
    directories = args[dir_index:]
    if "-f" in args:
        file_index = args.index("-f")
        directories = args[dir_index:file_index]
    dir_path = os.path.join(*directories)
    os.makedirs(dir_path, exist_ok=True)
if "-f" in args:
    file_index = args.index("-f") + 1
    file_name = args[file_index]
    file_path = os.path.join(dir_path, file_name)

    with open(file_path, "a") as file:
        file.write(f"{date_today}\n")
        counter = 1
        while True:
            text = input("Enter content line: ")
            if text.lower() == "stop":
                break
            file.write(f"{counter} {text}\n")
            counter += 1
