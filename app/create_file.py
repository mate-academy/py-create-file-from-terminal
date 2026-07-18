import os
import sys
from datetime import datetime

arguments = sys.argv
dir_path = ""

if "-d" in arguments:
    dirs = []
    start = arguments.index("-d")

    for arg in arguments[start + 1:]:
        if arg == "-f":
            break

        dirs.append(arg)

    dir_path = os.path.join(*dirs)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

if "-f" in arguments:
    file_name = arguments[arguments.index("-f") + 1]

    if dir_path:
        file_name = os.path.join(dir_path, file_name)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a+") as file:
        file.seek(0)
        first_char = file.read(1)

        if first_char:
            file.write("\n\n")

        file.write(timestamp)
        line_counter = 0

        while True:
            entered_text = input("Enter content line: ")

            if entered_text == "stop":
                break

            line_counter += 1

            file.write("\n" + str(line_counter) + " " + entered_text)
