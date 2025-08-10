import os
import sys
from datetime import datetime


def make_file(filename: str) -> None:
    line = 1
    with open(filename, "a") as file:
        if file.tell() != 0:
            file.write("\n\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        while 1:
            file_content = input("Enter content line:")
            if file_content == "stop":
                break

            file.write(f"\n{line} {file_content}")
            line += 1


def make_and_change_dirs(directories: list) -> None:
    os.makedirs(os.path.join(*directories), exist_ok=True)
    os.chdir(os.path.join(*directories))


def find_flag_index(cmd_args: list, flag: str) -> int:
    try:
        flag_index = cmd_args.index(flag)
    except ValueError:
        flag_index = None
    return flag_index


def make_filename(cmd_args: list, f_flag_index: int) -> str:
    return cmd_args[f_flag_index + 1]


def parse_and_create_data() -> None:
    cmd_args = sys.argv
    d_flag = "-d"
    f_flag = "-f"
    directories, filename = "", ""

    d_flag_index = find_flag_index(cmd_args, d_flag)
    f_flag_index = find_flag_index(cmd_args, f_flag)

    if d_flag in cmd_args and f_flag in cmd_args:
        if f_flag_index < d_flag_index:
            directories = cmd_args[d_flag_index + 1:]
        elif d_flag_index < f_flag_index:
            directories = cmd_args[d_flag_index + 1:f_flag_index]

        filename = make_filename(cmd_args, f_flag_index)

    elif d_flag in cmd_args:
        directories = cmd_args[d_flag_index + 1:]

    elif f_flag in cmd_args:
        filename = make_filename(cmd_args, f_flag_index)

    if directories:
        make_and_change_dirs(directories)
    if filename:
        make_file(filename)


if __name__ == "__main__":
    parse_and_create_data()
