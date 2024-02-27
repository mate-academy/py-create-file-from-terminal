import os
import sys
from datetime import datetime


def make_file(filename: str) -> None:
    line_number = 1
    with open(filename, "a") as file:
        if file.tell() != 0:
            file.write("\n\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        while 1:
            file_content = input("Enter content line:")
            if file_content == "stop":
                break

            file.write(f"\n{line_number} {file_content}")
            line_number += 1


def make_and_change_dirs(directories: list) -> None:
    os.makedirs(os.path.join(*directories), exist_ok=True)
    os.chdir(os.path.join(*directories))


def find_flag_index(cmd_args: list, flag: str) -> int:
    try:
        flag_index = cmd_args.index(flag)
    except ValueError:
        flag_index = None
    return flag_index


def parse_and_create_data() -> None:
    cmd_args = sys.argv
    d_flag = "-d"
    f_flag = "-f"
    directories = ""

    d_flag_index = find_flag_index(cmd_args, d_flag)
    f_flag_index = find_flag_index(cmd_args, f_flag)

    if d_flag in cmd_args and f_flag in cmd_args:
        if f_flag_index < d_flag_index:
            directories = cmd_args[d_flag_index + 1:]
        elif d_flag_index < f_flag_index:
            directories = cmd_args[d_flag_index + 1:f_flag_index]

        filename = cmd_args[f_flag_index + 1]

        make_and_change_dirs(directories)
        make_file(filename)

    elif d_flag in cmd_args:
        directories = cmd_args[d_flag_index + 1:]

        make_and_change_dirs(directories)

    elif f_flag in cmd_args:
        filename = cmd_args[f_flag_index + 1]

        make_file(filename)


if __name__ == "__main__":
    parse_and_create_data()
