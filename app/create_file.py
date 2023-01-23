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


def create_or_get_dir() -> str:
    path = os.getcwd()
    if "-d" in sys.argv:
        for i in range(sys.argv.index("-d") + 1, len(sys.argv)):
            if sys.argv[i] == "-f":
                break
            path = os.path.join(path, sys.argv[i])
        os.makedirs(path, exist_ok=True)
    return path


def creating_file() -> None:
    path = os.path.join(
        create_or_get_dir(),
        sys.argv[sys.argv.index("-f") + 1]
    )
    now = datetime.now()
    now_string = datetime.strftime(now, "%Y-%m-%d %H:%M:%S")
    with open(path, "a") as file:
        file.write(f"{now_string}\n")
        file.write(add_info())
        file.write("\n")


if "-d" in sys.argv and "-f" not in sys.argv:
    create_or_get_dir()
elif "-f" in sys.argv:
    creating_file()
