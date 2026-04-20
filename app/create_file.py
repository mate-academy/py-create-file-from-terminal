import os
import sys
from datetime import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        while True:
            user_line = input("Enter content line: ")
            if user_line == "stop":
                break
            f.write(user_line + "\n")


if "-d" in sys.argv and "-f" in sys.argv:
    d_index = sys.argv.index("-d")
    f_index = sys.argv.index("-f")

    file_directory = os.path.join(*sys.argv[d_index + 1:f_index])
    file_name = sys.argv[-1]

    if not os.path.exists(file_directory):
        os.makedirs(file_directory)
    create_file(os.path.join(file_directory, file_name))

elif "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    file_name = sys.argv[-1]

    create_file(file_name)
elif "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    file_directory = os.path.join(*sys.argv[d_index + 1:])

    if not os.path.exists(file_directory):
        os.makedirs(file_directory)
