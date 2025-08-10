import datetime
import os
import sys


def direction_create(d_flag: int, f_flag: int | None, args: list) -> str:
    if f_flag and f_flag > d_flag:
        dirs = args[d_flag + 1: f_flag]
    else:
        dirs = args[d_flag + 1:]

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

    return path


def add_some_info_in_file(file_name: str, path: str) -> None:
    with open(os.path.join(path, file_name), "a") as file:
        strf_now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{strf_now_time}\n")
        row = 1
        while True:
            text = input("Write your text: ")
            if text == "stop":
                file.write("\n")
                break
            file.write(f"{row} {text}\n")
            row += 1


args = sys.argv
d_flag = args.index("-d") if "-d" in args else None
f_flag = args.index("-f") if "-f" in args else None
path = ""

if d_flag:
    path = direction_create(d_flag, f_flag, args)

if f_flag:
    add_some_info_in_file(args[f_flag + 1], path)
