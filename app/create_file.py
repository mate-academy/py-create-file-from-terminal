import os
import sys
import datetime


arguments = sys.argv[1:]
path = []

if "-d" in arguments:
    id_index = arguments.index("-d")
    if id_index + 1 >= len(arguments) or arguments[id_index + 1] == "-f":
        sys.exit(1)
    for directory in arguments[id_index + 1:]:
        if directory == "-f":
            break
        path.append(directory)

    dir_path = os.path.join(*path)
    os.makedirs(dir_path, exists_ok=True)

if "-f" in arguments:
    if arguments.index("-f") + 1 >= len(arguments):
        sys.exit(1)
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
