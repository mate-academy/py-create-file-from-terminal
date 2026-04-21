import argparse
import os
from datetime import datetime


def create_directory(dir_list: list) -> None:
    path = os.path.join(*dir_list)
    os.makedirs(path, exist_ok=True)


def write_content(file_name: str) -> None:
    lines = []
    line = 0
    while True:
        content = input("Enter content line:")
        if content == "stop":
            break
        line += 1
        lines.append(f"{line} {content}")

    with open(file_name, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        file.write("\n".join(lines))
        file.write("\n")


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs="+")
    parser.add_argument("-f")
    args = parser.parse_args()

    if args.d:
        dir_list = args.d
        create_directory(dir_list)

    if args.f:
        file_name = args.f
        if args.d:
            file_name = os.path.join(*dir_list, file_name)
        write_content(file_name)


if __name__ == "__main__":
    create_file()
