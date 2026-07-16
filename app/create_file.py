import sys
import os
import datetime


def terminal_flags_controller():
    arguments = sys.argv

    if "-d" in arguments and "-f" in arguments:
        path_list = arguments[2:-2]
        file_name = arguments[-1]
        new_path = new_path_creation(path_list)
        new_dir_file = os.path.join(new_path, file_name)
        new_file_creation(new_dir_file)

    if "-d" in arguments:
        new_path_creation(arguments[2:])

    if "-f" in arguments:
        new_file_creation(arguments[2])


def new_path_creation(directories: list):
    path = os.path.join(*directories)

    if not os.path.exists:
        os.makedirs(path)

    return path


def new_file_creation(file_name: str):
    with open(file_name, "a") as f:
        local_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(local_time + "\n")
        line_number = 1

        while True:
            line_content = input("Enter content line: ")

            if line_content == "stop":
                f.write("\n")
                break

            else:
                f.write(f"{line_number} {line_content}\n")
                line_number += 1
