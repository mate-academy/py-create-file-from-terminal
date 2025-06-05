import os
import sys
import datetime


args = sys.argv


def is_valid_flag(args: list, flag: str) -> int:
    try:
        index = args.index(flag)
        if index + 1 < len(args) and not args[index + 1].startswith("-"):
            return index
    except ValueError:
        return None


d_index = is_valid_flag(args, "-d")
f_index = is_valid_flag(args, "-f")


if d_index is not None:
    if f_index is not None:
        if f_index > d_index:
            dir_path = os.path.join(*args[d_index + 1:f_index])
        elif f_index < d_index:
            dir_path = os.path.join(*args[d_index + 1:])
    else:
        dir_path = os.path.join(*args[d_index + 1:])
    os.makedirs(dir_path, exist_ok=True)


if f_index is not None:
    file_name = args[f_index + 1]

    if d_index is not None:
        path_to_file = os.path.join(dir_path, file_name)
    else:
        path_to_file = file_name

    with open(path_to_file, "a", encoding="utf-8") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        while True:
            line = input()
            if line == "stop":
                break
            else:
                f.write(line + "\n")
