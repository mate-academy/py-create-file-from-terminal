import os
import sys
from datetime import datetime


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

    d_args = []
    if d_flag_is_used:
        try:
            d_index = args.index("-d") + 1
            while d_index < len(args) and args[d_index][0] != "-":
                d_args.append(args[d_index])
                d_index += 1
        except IndexError:
            print("Flag '-d' was used but no parameters were given")
            return

    filepath = create_path(["."] + d_args) if d_flag_is_used else "./"
    filename = f_arg if f_flag_is_used else None

    if f_flag_is_used and filename is None:
        print("Flag '-f' was used but no parameters were given")
        return

    full_filepath = os.path.join(
        filepath, filename if filename else "file.txt"
    )

    if d_flag_is_used and not os.path.isdir(filepath):
        try:
            os.makedirs(filepath)
        except OSError as e:
            print("Error during directory creation:", e)
            return

    fill_data(full_filepath)


def create_path(directories: list) -> str:
    return os.path.join(*directories)


def fill_data(full_filepath: str) -> None:
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
