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


def create_path_regard_status(*flag_status: bool) -> str:
    f_flag_status, d_flag_status = flag_status
    path = ""
    if all(flag_status):
        first_dir = sys.argv.index("-d") + 1
        last_dir = sys.argv.index("-f")
        directories = sys.argv[first_dir:last_dir]
        path = os.path.join(*directories)

    if d_flag_status and not f_flag_status:
        directories = sys.argv[sys.argv.index("-d") + 1:]
        path = os.path.join(*directories)

    return path


flag_f = "-f" in sys.argv
flag_d = "-d" in sys.argv

if flag_f and not flag_d:
    filename = sys.argv[-1]
    if not os.path.exists(filename):
        write_content_to_file(filename, "w")
    else:
        write_content_to_file(filename, "a")
if flag_d and not flag_f:
    new_path = create_path_regard_status(flag_f, flag_d)
    os.makedirs(new_path, exist_ok=True)
if flag_f and flag_d:
    new_path = create_path_regard_status(flag_f, flag_d)
    os.makedirs(new_path, exist_ok=True)
    path_to_file = os.path.join(new_path, sys.argv[-1])
    write_content_to_file(path_to_file, "w")
