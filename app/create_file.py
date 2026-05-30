import os
import sys
from datetime import datetime
from typing import Union, Optional


def create_path(dirs: list) -> Optional[str]:
    return os.path.join(*dirs)


def check_for_flag(command: list[str], flag: str) -> Union[int, None]:
    try:
        return command.index(flag, 1)
    except ValueError:
        return None


def create_folders(
        ind_f_flag: Union[int, None],
        ind_d_flag: Union[int, None]
) -> list[str]:
    if not ind_d_flag:
        return []
    if not ind_f_flag or (ind_f_flag and ind_f_flag < ind_d_flag):
        dir_list = command[ind_d_flag + 1:]
    else:
        dir_list = command[ind_d_flag + 1:ind_f_flag]
    os.makedirs(create_path(dir_list), exist_ok=True)
    return dir_list


def write_terminal_to_file(filename: str) -> None:
    with open(filename, "a") as file:
        line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(
            f"\n{line}\n" if os.path.getsize(filename) > 0 else f"{line}\n"
        )
        counter = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{str(counter)} {line}\n")
            counter += 1


command = sys.argv

ind_md = check_for_flag(command, "-d")
ind_mf = check_for_flag(command, "-f")

path_list = create_folders(ind_mf, ind_md)
if ind_mf:
    full_file_name = create_path(path_list + command[ind_mf + 1:ind_mf + 2])
    write_terminal_to_file(full_file_name)
