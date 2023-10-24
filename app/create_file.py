import os
import sys
from datetime import datetime


module_args = sys.argv


def get_f_flag_index() -> int:
    if "-f" in module_args:
        return module_args.index("-f")


def get_d_flag_index() -> int:
    if "-d" in module_args:
        return module_args.index("-d")


def get_file_name(f_index: int | None, d_index: int | None) -> str:
    if f_index and d_index:
        return os.path.join(
            *module_args[d_index + 1:f_index], module_args[f_index + 1]
        )
    if f_index:
        return module_args[f_index + 1]


def create_dirs(f_index: int | None, d_index: int | None) -> None:
    user_dirs = None

    if f_index and d_index:
        user_dirs = module_args[d_index + 1:f_index]
    if not f_index and d_index:
        user_dirs = module_args[d_index + 1:]

    if user_dirs:
        dir_path = os.path.join(*user_dirs)
        os.makedirs(dir_path)


def write_into_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        while True:
            line_number = 1
            user_input = input("Enter content line: ")

            if user_input == "stop":
                break

            file.write(f"{line_number} {user_input}\n")
            line_number += 1


if __name__ == "__main__":
    f_index = get_f_flag_index()
    d_index = get_d_flag_index()

    file_name = get_file_name(f_index, d_index)

    create_dirs(f_index, d_index)
    if file_name:
        write_into_file(file_name)
