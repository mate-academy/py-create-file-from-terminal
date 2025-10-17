import sys
import os
import datetime


sys_args = sys.argv


def make_file(path: str) -> None:
    mode, indent = ("a", "\n") if os.path.exists(path) else ("w", "")
    with open(path_to_file, mode) as file_append:
        file_append.write(
            f"{indent}"
            f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n"
        )
        while True:
            message = input("Enter content line: ")
            if message == "stop":
                break
            file_append.write(message + "\n")


if "-f" in sys_args:
    f_index = sys_args.index("-f")
    if "-d" in sys_args:
        d_index = sys_args.index("-d")
        path = os.path.join(*sys_args[d_index + 1: f_index])
        os.makedirs(path, exist_ok=True)
        path_to_file = os.path.join(path, sys_args[f_index + 1])
        make_file(path_to_file)
    else:
        path_to_file = os.path.join(*sys_args[f_index + 1:])
        print(*sys_args[f_index + 1:])
        make_file(path_to_file)
elif "-d" in sys_args:
    d_index = sys_args.index("-d")
    path = os.path.join(*sys_args[d_index + 1:])
    os.makedirs(path, exist_ok=True)
