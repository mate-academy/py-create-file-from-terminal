import os
import sys
import datetime


arguments = sys.argv[1:]
path = []

if "-d" in arguments:
    for directory in arguments[2:]:
        if directory == "-f":
            break
        path.append(directory)
    os.makedirs("/".join(path), exist_ok=True)

path_to_file = "/".join(path) + "/" + arguments[-1]

if "-f" in arguments:
    with open(path_to_file, "a") as file:
        current_date = datetime.datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S\n"))
        number_line = 0
        while True:
            file_content = input("Enter content line: ")
            if file_content == "stop":
                break
            number_line += 1
            file.write(f"{number_line} {file_content}\n")
