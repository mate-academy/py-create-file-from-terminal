import os
import sys
from datetime import datetime


def parse() -> None:
    argv = sys.argv[1:]
    dir_path = ""
    filename = None

    if "-f" in argv:
        index = argv.index("-f")
        filename = argv[index + 1]
        argv.remove("-f")
        argv.remove(filename)

    if "-d" in argv:
        index = argv.index("-d")
        print(argv)
        dir_path = os.path.join(*argv[index + 1:])

    if dir_path:
        create_dir(dir_path)

    if filename:
        file_path = os.path.join(dir_path, filename)
        create_file(file_path)


def create_dir(dir_path: str) -> None:
    os.mkdir(dir_path)


def content() -> list:
    lines = [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    line_count = 1
    while True:
        line = input("Enter content line:")
        if line == "stop":
            break
        lines.append(f"{line_count} {line}")
        line_count += 1

    return lines


def create_file(file_path: str) -> None:
    with open(file_path, "w") as file:
        for line in content():
            file.write(line + "\n")


parse()
