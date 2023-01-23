import sys
import os
from datetime import datetime


def add_info() -> str:
    line_num = 0
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        line_num += 1
        lines.append(f"{line_num} {line}")
    return "\n".join(lines) + "\n"


def create_or_get_dir(f_flag: bool) -> str:
    path = os.getcwd()
    if "-d" in sys.argv:
        index_d = sys.argv.index("-d")
        if f_flag:
            index_f = sys.argv.index("-f")
            path = os.path.join(path, *sys.argv[index_d + 1:index_f])
        else:
            path = os.path.join(path, *sys.argv[index_d + 1:])
        os.makedirs(path, exist_ok=True)
    return path


def creating_file() -> None:
    path = os.path.join(
        create_or_get_dir(f_flag=True),
        sys.argv[sys.argv.index("-f") + 1]
    )
    now = datetime.now()
    now_string = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
    with open(path, "a") as file:
        file.write(f"{now_string}\n")
        file.write(add_info())
        file.write("\n")


if "-d" in sys.argv and "-f" not in sys.argv:
    create_or_get_dir(f_flag=False)
elif "-f" in sys.argv:
    creating_file()
