import sys
import os
import datetime

arg = sys.argv


def create_file(directory_path: str) -> None:
    with open(directory_path, "a") as file:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{current_time}\n")
        line_counter = 1
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"{line_counter} {new_line}\n")
            line_counter += 1

dir_path = []
file_name = None
path = os.getcwd()

if "-d" in arg and "-f" not in arg:
    d_index = arg.index("-d")
    direct = arg[d_index + 1:]
    path = os.path.join(*direct)
    os.makedirs(path, exist_ok=True)

if "-f" in arg and "-d" not in arg:
    f_index = arg.index("-f")
    file_name = arg[f_index + 1]
    create_file(file_name)

if "-d" in arg and "-f" in arg:
    d_index = arg.index("-d")
    f_index = arg.index("-f")
    if arg.index("-d") > arg.index("-f"):
        direct = arg[d_index + 1:]
        file_name = arg[f_index + 1]
        path = os.path.join(*direct)
        os.makedirs(path, exist_ok=True)
    else:
        direct = arg[d_index + 1: f_index]
        file_name = arg[f_index + 1]
        path = os.path.join(*direct)
        os.makedirs(path, exist_ok=True)

    create_file(os.path.join(path, file_name))
