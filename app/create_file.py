import datetime
import os
import sys


def create_dirs(flag_d: int, flag_f: int | None, args: list) -> str:
    if flag_f and flag_f > flag_d:
        dirs = args[flag_d + 1: flag_f]
    else:
        dirs = args[flag_d + 1:]

    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

    return path


def add_data_in_file(file_name: str, path: str) -> None:
    with open(os.path.join(path, file_name), "a") as file:
        time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time_now}\n")
        line = 1
        while True:
            text = input("Write your text: ")
            if text == "stop":
                file.write("\n")
                break
            file.write(f"{line} {text}\n")
            line += 1


args = sys.argv
flag_d = args.index("-d") if "-d" in args else None
flag_f = args.index("-f") if "-f" in args else None
path = ""

if flag_d:
    path = create_dirs(flag_d, flag_f, args)

if flag_f:
    add_data_in_file(args[flag_f + 1], path)
