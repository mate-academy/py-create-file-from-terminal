import sys
from datetime import datetime
import os


current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

file_name_directory = sys.argv[2:]
file_name_directory = os.path.join(*file_name_directory)


if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    dir_path = os.path.join(*sys.argv[d_index + 1:])
    os.makedirs(dir_path)

if "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[f_index + 1]
    file_path = file_name

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        dir_path = os.path.join(*sys.argv[d_index + 1:f_index])
        file_path = os.path.join(dir_path, file_name)

    with open(file_path, "a") as file:
        line_number = 0
        file.write(f"{formatted_time}\n")

        while True:
            file_input = input("Enter content line: ")
            if file_input == "stop":
                break
            line_number += 1
            file.write(f"Line{line_number} {file_input}\n")

