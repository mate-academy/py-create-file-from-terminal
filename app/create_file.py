import os
import sys
import datetime

arguments = sys.argv
file_name = ""
current_dir = os.getcwd()

if "-f" in arguments:
    file_name = arguments[arguments.index("-f") + 1]
    arguments.pop(arguments.index("-f") + 1)
    arguments.pop(arguments.index("-f"))

if "-d" in arguments:
    for directory in arguments[arguments.index("-d") + 1:]:
        current_dir = os.path.join(current_dir, directory)
    if not os.path.exists(current_dir):
        os.makedirs(current_dir)

if file_name:
    file_path = os.path.join(current_dir, file_name)
    with open(file_path, "a") as source_file:
        if os.path.getsize(file_path) != 0:
            source_file.write("\n")
        source_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        line_number = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line.lower() == "stop":
                break
            source_file.write(f"{line_number} {new_line}\n")
            line_number += 1
