import os

import datetime

import sys


def write_content_to_file(filepath: str, mode: str) -> None:
    with open(filepath, mode) as file_in:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_in.write(f"{time_now}\n")
        counter = 0
        while True:
            content = input("Enter content line: ")
            counter += 1
            if content == "stop":
                break

            file_in.write(f"{counter} {content}\n")


# filename = sys.argv[-1]
flag_f = "-f" in sys.argv
flag_d = "-d" in sys.argv

if flag_f and not flag_d:
    filename = sys.argv[-1]
    if not os.path.exists(filename):
        write_content_to_file(filename, "w")
    else:
        write_content_to_file(filename, "a")
if flag_d and not flag_f:
    dir_names = "/".join(sys.argv[sys.argv.index("-d") + 1:])
    new_path = os.path.abspath(dir_names)
    os.makedirs(new_path, exist_ok=True)
if flag_f and flag_d:
    first_dir_index = sys.argv.index("-d") + 1
    last_dir_index = sys.argv.index("-f")
    dir_names = "/".join(sys.argv[first_dir_index:last_dir_index])
    new_path = os.path.abspath(dir_names)
    os.makedirs(new_path, exist_ok=True)
    write_content_to_file(new_path + sys.argv[-1], "w")
