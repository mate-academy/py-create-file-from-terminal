import os
import sys
from datetime import datetime


def make_directories(dirs: list) -> None:
    return os.makedirs(os.path.join(*dirs), exist_ok=True)


def input_file_contents(path_name: str) -> None:
    with open(path_name, "a") as file:
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(time_now)
        line_number = 0
        while True:
            line_number += 1
            content = input("Enter content line: ")
            if content == "stop":
                file.write("\n\n")
                break
            file.write(f"\n{line_number} {content}")


if "-d" in sys.argv and "-f" in sys.argv:
    d_flag_index = sys.argv.index("-d")
    f_flag_index = sys.argv.index("-f")
    if f_flag_index > d_flag_index:
        directories = sys.argv[2:-2]
        file_name = sys.argv[-1]
    else:
        directories = sys.argv[d_flag_index + 1:]
        file_name = sys.argv[2]

    make_directories(directories)
    joined_path = os.path.join(*directories, file_name)
    input_file_contents(joined_path)

elif "-d" in sys.argv:
    directories = sys.argv[2:]
    make_directories(directories)

elif "-f" in sys.argv:
    file_name = sys.argv[-1]
    input_file_contents(file_name)
