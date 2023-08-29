from datetime import datetime
import os
from sys import argv

if "-d" not in argv and "-f" not in argv:
    raise Exception("You should provide at least one flag")

directories = []
file_name = ""

if "-d" in argv:
    for value in range(argv.index("-d") + 1, len(argv)):
        if argv[value] == "-f":
            break

        directories.append(argv[value])
if "-f" in argv:
    file_name = argv[argv.index("-f") + 1]

path = ""

if directories:
    path = os.path.join(*directories)

    if not os.path.exists(path):
        os.makedirs(path)


if file_name:
    with open(os.path.join(path, file_name), "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        line_number = 1

        while True:
            entered_content = input("Enter content line: ")

            if entered_content == "stop":
                break

            file.write(f"{line_number} {entered_content}\n")
            line_number += 1
