import sys
import os
import datetime as dt


def create_directories(directories: list) -> str:
    dir_path = ""
    for directory in directories:
        dir_path = os.path.join(dir_path, directory)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


if "-f" not in sys.argv and "-d" not in sys.argv:
    print("Usage: python create_file.py -f <filename> or -d <directory>")
    sys.exit(1)

file_path = ""

d_flag_index = sys.argv.index("-d") if "-d" in sys.argv else None
f_flag_index = sys.argv.index("-f") if "-f" in sys.argv else None

if d_flag_index is not None:
    last_dir_index = len(sys.argv) - 1

    if (
        d_flag_index + 1 >= len(sys.argv) or
        sys.argv[d_flag_index + 1].startswith("-")
    ):
        print("Error: '-d' flag provided but no directory specified.")
        sys.exit(1)

    if f_flag_index is not None and f_flag_index > d_flag_index:
        last_dir_index = min(f_flag_index - 1, last_dir_index)

    directories = sys.argv[d_flag_index + 1:last_dir_index + 1]
    file_path = create_directories(directories)

if f_flag_index is not None:
    if f_flag_index + 1 >= len(sys.argv):
        print("Error: '-f' flag provided but no filename specified.")
        sys.exit(1)
    elif f_flag_index + 1 == d_flag_index:
        print(
            "Error: '-f' flag provided but no filename specified "
            "(next argument is '-d')."
        )
        sys.exit(1)

    filename = sys.argv[f_flag_index + 1]

    if os.path.isdir(filename):
        print("Error: Specified filename is a directory.")
        sys.exit(1)

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
            counter += 1
