import sys
import os
from datetime import datetime


def make_a_file(name: str, path: str) -> None:

    path_to_file = os.path.join(path, name)

    if os.path.exists(path_to_file):
        method_add = "a"
    else:
        method_add = "w"

    with open(path_to_file, method_add) as file:
        line = 0
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))

        while True:
            line += 1
            message = input("Enter content line: ")

            if message.lower() == "stop":
                file.write("\n")
                break

            file.write(f"{line} {message}\n")


if "-d" in sys.argv and "-f" in sys.argv:

    i = 2
    dirs = []

    while sys.argv[i] != "-f":
        dirs.append(sys.argv[i])
        i += 1

    file_name = sys.argv[i + 1]

    dirs_path = os.path.join(*dirs)
    os.makedirs(dirs_path)
    make_a_file(file_name, dirs_path)

elif "-d" in sys.argv:
    dirs_path = os.path.join(*sys.argv[2:])
    os.makedirs(dirs_path)

elif "-f" in sys.argv:
    file_name = sys.argv[2]
    current_directory = os.getcwd()
    make_a_file(file_name, current_directory)
