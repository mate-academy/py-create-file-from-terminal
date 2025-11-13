import sys
import os
from datetime import datetime


def parse_command_arguments() -> tuple:
    cmd_args = sys.argv
    flag_f_inx = cmd_args.index("-f") if "-f" in cmd_args else -1
    flag_d_inx = cmd_args.index("-d") if "-d" in cmd_args else -1

    file_name = ""
    directory_parts = []

    # 1. -f
    if flag_d_inx == -1 and flag_f_inx != -1:
        if flag_f_inx + 1 < len(cmd_args):
            file_name = cmd_args[flag_f_inx + 1]

    # 2. -d
    elif flag_d_inx != -1 and flag_f_inx == -1:
        if flag_d_inx + 1 < len(cmd_args):
            directory_parts = cmd_args[flag_d_inx + 1:]
    # 3. -f -d
    elif flag_d_inx > flag_f_inx:
        if flag_d_inx + 1 < len(cmd_args):
            file_name = cmd_args[flag_f_inx + 1]
            directory_parts = cmd_args[flag_d_inx + 1:]
    # 4. -d -f
    elif flag_f_inx > flag_d_inx:
        file_name = cmd_args[flag_f_inx + 1]
        directory_parts = cmd_args[flag_d_inx + 1: flag_f_inx]

    return directory_parts, file_name


def create_directory(directory_parts: list) -> str:
    directory_path = ""
    if directory_parts:
        directory_path = os.path.join(*directory_parts)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
    return directory_path


def write_to_file(file_name: str, directory_path: str) -> None:
    full_file_name = os.path.join(directory_path, file_name)
    if full_file_name:
        with open(full_file_name, "a") as source_file:
            source_file.write(
                f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
            )
            i = 1
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                source_file.write(f"{i} {line}\n")
                i += 1


#
if __name__ == "__main__":
    directory_parts_, file_name_ = parse_command_arguments()
    directory_path_ = create_directory(directory_parts_)
    write_to_file(file_name_, directory_path_)
