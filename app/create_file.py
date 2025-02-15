import os
import sys
import datetime


arguments = sys.argv[1:]
path = []

if "-id" in arguments:
    id_index = arguments.index("-id")
    for directory in arguments[id_index + 1:]:
        if directory == "-f":
            break
        path.append(directory)

    os.makedirs(os.path.join(*path), exists_ok=True)

if "-f" in arguments:
    filename = arguments[arguments.index("-f") + 1]
    path_to_file = os.path.join(*path, filename)

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
