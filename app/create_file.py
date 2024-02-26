import os
import sys
from datetime import datetime


def make_file(filename: str) -> None:
    line_number = 1
    with open(filename, "a") as f:
        if f.tell() != 0:
            f.write("\n\n")

        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        while 1:
            inp = input("Enter content line:")
            if inp == "stop":
                break

            f.write(f"\n{line_number} {inp}")
            line_number += 1


def make_dirs(directories: list) -> None:
    for directory in directories:
        os.makedirs(directory)
        os.chdir(directory)


def create_filename_with_index() -> str:
    cmd_args, _, f_flag = get_args_and_flags()
    flag_index = cmd_args.index(f_flag)
    filename = cmd_args[flag_index + 1]
    return filename


def create_dirs_with_index() -> list:
    cmd_args, d_flag, _ = get_args_and_flags()
    flag_index = cmd_args.index(d_flag)
    directories = cmd_args[flag_index + 1:]
    return directories


def get_args_and_flags() -> tuple:
    cmd_args = sys.argv
    d_flag = "-d"
    f_flag = "-f"
    return cmd_args, d_flag, f_flag


def main() -> None:
    cmd_args, d_flag, f_flag = get_args_and_flags()

    if d_flag in cmd_args and f_flag in cmd_args:
        d_flag_index = cmd_args.index(d_flag)
        f_flag_index = cmd_args.index(f_flag)

        if f_flag_index < d_flag_index:
            directories = cmd_args[d_flag_index + 1:]
        else:
            directories = cmd_args[d_flag_index + 1:f_flag_index]
        filename = cmd_args[f_flag_index + 1]

        make_dirs(directories)
        make_file(filename)

    elif d_flag in cmd_args:
        print('d')
        directories = create_dirs_with_index()
        make_dirs(directories)

    elif f_flag in cmd_args:
        filename = create_filename_with_index()
        make_file(filename)


if __name__ == "__main__":
    main()
