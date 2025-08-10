import os
import sys
from datetime import datetime
from typing import Union, LiteralString


def main() -> None:
    args = sys.argv

    d_flag_is_used = "-d" in args
    f_flag_is_used = "-f" in args

    if not (d_flag_is_used or f_flag_is_used):
        print("Flag '-f' or '-d' must be used but no flags were given")
        return

    f_arg = None
    if f_flag_is_used:
        try:
            f_arg = args[args.index("-f") + 1]
            if f_arg == "-d":
                raise IndexError

        except IndexError:
            print("Flag '-f' was used but no parameters were given")
            return

    d_args = list()
    if d_flag_is_used:
        d_args = args[args.index("-d") + 1:(args.index("-f")
                      if f_flag_is_used and args.index("-f") > args.index("-d")
                      else None)]
        if not len(d_args):
            print("Flag '-d' was used but no parameters were given")
            return

    filepath = create_path(["."] + d_args + [""]) if d_flag_is_used else "./"
    filename = f_arg if f_flag_is_used else "file.txt"
    full_filepath = filepath + filename

    if d_flag_is_used and not os.path.isdir(filepath):
        try:
            os.makedirs(filepath)
        except OSError as e:
            print("Error during directory creation:", e)
            return

    fill_data(full_filepath)


def create_path(directories: list) -> Union[str, LiteralString, bytes]:
    path = os.path.join(*directories)
    return path


def fill_data(full_filepath: Union[str, LiteralString, bytes]) -> None:
    file_exists = os.path.exists(full_filepath)

    with open(full_filepath, "a+") as file:

        if file_exists:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        row_number = 1

        while True:
            data_to_write = input("Enter content line: ")
            if data_to_write == "stop":
                break
            file.write(f"{row_number} {data_to_write}\n")
            row_number += 1


if __name__ == "__main__":
    main()
