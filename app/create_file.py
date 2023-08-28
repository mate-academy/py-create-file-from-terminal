import sys
import os
import datetime


def create_file(name_file: str) -> None:
    with open(name_file, "a") as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_number = 0
        while (input_str := input("Enter content line: ")) != "stop":
            file.write(f"{line_number} {input_str}" + "\n")
            file.write("\n")
            line_number += 1


def create_dir(path_dir: list) -> None:
    path = os.path.join(*path_dir)
    os.makedirs(path, exist_ok=True)
    os.chdir(path)


if __name__ == "__main__":
    info_from_terminal = sys.argv

    if "-d" in info_from_terminal and "-f" in info_from_terminal:
        index_d = info_from_terminal.index("-d")
        index_f = info_from_terminal.index("-f")

        if index_d < index_f:
            create_dir(info_from_terminal[index_d + 1: index_f])
            create_file(info_from_terminal[-1])
        else:
            create_dir(info_from_terminal[index_d + 1:])
            create_file(info_from_terminal[index_f + 1])

    elif "-d" in info_from_terminal:
        index_start = info_from_terminal.index("-d")
        create_dir(info_from_terminal[index_start + 1:])

    elif "-f" in info_from_terminal:
        create_file(info_from_terminal[1])
