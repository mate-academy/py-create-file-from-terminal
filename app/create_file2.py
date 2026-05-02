from sys import argv
import os
import datetime as dt


def create_directories(directories: list) -> str:
    dir_path = ""
    for directory in directories:
        dir_path = os.path.join(dir_path, directory)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


if "-f" not in argv and "-d" not in argv:
    print("Usage: python create_file.py -f <filename> or -d <directory>")
    exit(1)

file_path = ""
directories = []
f_flag_index = 0

d_flag_index = argv.index("-d") if "-d" in argv else None
f_flag_index = argv.index("-f") if "-f" in argv else None

if d_flag_index is not None:
    last_dir_index = len(argv) - 1

    if d_flag_index + 1 >= len(argv):
        print("Error: '-d' flag provided but no directory specified.")
        exit(1)

for directory in argv[d_flag_index + 1:]:
    if directory.startswith("-"):
        break
    directories.append(directory)

file_path = create_directories(directories)

if f_flag_index is  None:
    exit(1)
if f_flag_index >= len(argv) - 1:
    print("Error: '-f' flag provided but no filename specified.")
    exit(1)
elif f_flag_index + 1 == d_flag_index:
    print(
        "Error: '-f' flag provided but no filename specified "
        "(next argument is '-d')."
    )
    exit(1)

filename = argv[f_flag_index + 1]

if os.path.isdir(filename):
    print("Error: Specified filename is a directory.")
    exit(1)

file_path = os.path.join(file_path, filename) if file_path else filename

is_append_mode = os.path.exists(file_path)

with open(file_path, "a") as file:
    time_stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if is_append_mode:
        file.write("\n")
    file.write(f"{time_stamp}\n")

    token = ""
    counter = 1

    while True:
        token = input("Enter content line: ")
        if token == "stop":
            # file.write("\n")
            break
        file.write(f"{counter} {token}\n")