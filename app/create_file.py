import os
import sys
import datetime


def create_file() -> None:
    full_path = ""
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d") + 1
        if "-f" in sys.argv:
            f_index = sys.argv.index("-f") +1
            dir_pars = sys.argv[d_index:f_index]
        else:
            dir_pars = sys.argv[d_index:]

    file_name = ""
    if "-f" in sys.argv:
        f_index = sys.argv.index("-f") + 1
        file_name = sys.argv[f_index]

    if not os.path.isdir(full_path):
        os.makedirs(full_path)

    if file_name == "":
        full_path = os.path.join(full_path, "file.txt")
    else:
        full_path = os.path.join(full_path, file_name)

    input_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    count = 0
    while True:
        temp_str = input("Enter content line: ")
        if temp_str == "stop":
            break
        count += 1
        input_str += str(count)
        input_str += " " + temp_str + "\n"
    input_str += "\n"

    with open(full_path, "a") as file:
        file.write(input_str)
