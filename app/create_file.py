import os
import sys
import datetime
from typing import TextIO


def create_dir(directories: list[str]) -> str:
    dir_path = os.path.join(*directories)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    return dir_path


def write_in_file(file_obj: TextIO) -> None:
    i = 1
    file_obj.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
    while True:
        new_line = input("Enter content line: ")
        if new_line == "stop":
            break
        file_obj.write(f"{i} {new_line}\n")
        i += 1


def create_file(path: str) -> None:
    if not os.path.exists(path):
        with open(path, "w") as file:
            write_in_file(file)
    else:
        with open(path, "a") as file:
            file.write("\n")
            write_in_file(file)


def recognize_flags() -> None:
    command_args = sys.argv[1:]
    if not command_args:
        return

    if "-f" in command_args and "-d" in command_args:
        f_idx = command_args.index("-f")
        d_idx = command_args.index("-d")

        if f_idx < d_idx:
            file_name = command_args[f_idx + 1]
            directories = command_args[d_idx + 1:]
        else:
            directories = command_args[d_idx + 1:f_idx]
            file_name = command_args[f_idx + 1]

        target_dir = create_dir(directories)
        create_file(os.path.join(target_dir, file_name))

    elif "-d" in command_args:
        directories = command_args[command_args.index("-d") + 1:]
        create_dir(directories)

    elif "-f" in command_args:
        file_name = command_args[command_args.index("-f") + 1]
        create_file(os.path.join(os.getcwd(), file_name))


recognize_flags()
