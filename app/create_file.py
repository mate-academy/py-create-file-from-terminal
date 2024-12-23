import os
import sys
from datetime import datetime
from typing import TextIO


def create_file() -> None:
    current_dir = os.getcwd()
    dir_path = ""
    if "-d" in sys.argv and "-f" in sys.argv:
        d_index = sys.argv.index("-d")
        f_index = sys.argv.index("-f")
        d_params = sys.argv[d_index + 1:f_index]
        name_dir = os.path.join(current_dir, "/".join(d_params))

        if not os.path.exists(name_dir):
            os.makedirs(name_dir)

        dir_path = name_dir
    elif "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        d_params = sys.argv[d_index + 1:]
        name_dir = os.path.join(current_dir, "/".join(d_params))
        os.makedirs(name_dir)

        if not os.path.exists(name_dir):
            os.makedirs(name_dir)

        dir_path = name_dir

    if "-f" in sys.argv:
        f_name = sys.argv[sys.argv.index("-f") + 1:][0]
        if dir_path:
            file_path = dir_path + "/" + f_name
        else:
            file_path = f_name

        def read_input(file_to_process: TextIO) -> None:
            line_num = 1
            while True:
                user_input = input("Enter content line: ")
                if user_input == "stop":
                    break
                file_to_process.write(str(line_num) + " " + user_input + "\n")
                line_num += 1

        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                now = datetime.now()
                formatted_time = now.strftime("%Y-%m-%d %H:%M:%S" + "\n")
                file.write(formatted_time)
                read_input(file)
        else:
            with open(file_path, "a+") as file:
                now = datetime.now()
                formatted_time = now.strftime("%Y-%m-%d %H:%M:%S" + "\n")
                file.write("\n")
                file.write(formatted_time)
                read_input(file)
