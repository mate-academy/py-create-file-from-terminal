import sys
import os
from datetime import datetime


arguments = sys.argv
file_to_create = None
directories = []
result_dir = ""

if "-f" in arguments:
    file_to_create = arguments[arguments.index("-f") + 1]

if "-d" in arguments:
    for directory in arguments[arguments.index("-d") + 1:]:
        if directory == "-f":
            break
        directories.append(directory)

if directories:
    result_dir = os.path.join(os.getcwd(), *directories)
    os.makedirs(result_dir, exist_ok=True)

if file_to_create:
    file_path = os.path.join(os.getcwd(), result_dir, file_to_create)
    with open(file_path, "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_counter = 0
        while True:
            line_counter += 1
            answer = input("Enter content line: ")
            if answer == "stop":
                break
            f.write(f"\n{line_counter} {answer}")
