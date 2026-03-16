import sys

import os

import datetime


path = ""

if "-d" in sys.argv:
    index = sys.argv.index("-d")
    if "-f" in sys.argv:
        end_index = sys.argv.index("-f")
    else:
        end_index = len(sys.argv)
    file_path = sys.argv[index + 1: end_index]
    path = os.path.join(*file_path)
    os.makedirs(path, exist_ok=True)

if "-f" in sys.argv:
    index = sys.argv.index("-f")
    filename = sys.argv[index + 1]

    full_path = os.path.join(path, filename) if path else filename
    with open(full_path, "a") as output_file:
        if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
            output_file.write("\n")
        output_file.write(datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S") + "\n")
        line_num = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            line_num += 1
            output_file.write(str(line_num) + " " + line + "\n")
