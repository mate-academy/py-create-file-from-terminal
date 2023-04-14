import sys
import os

from datetime import datetime


def create_file(name_file: str) -> None:
    flag = "a" if os.path.exists(name_file) else "w"
    with open(name_file, flag) as file:
        first_line = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if flag != "w":
            first_line = "\n" + first_line
        file.write(first_line)
        line = ""
        line_number = 1
        while line != "stop":
            line = input("Enter content line: ")
            if line != "stop":
                file.write("\n" + str(line_number) + " " + line)
                line_number += 1
        file.write("\n")


def create_dirs(path_dir: list) -> None:
    path = os.path.join(*path_dir)
    os.makedirs(path, exist_ok=True)
    os.chdir(path)


if __name__ == "__main__":
    command = sys.argv
    if "-d" in command and "-f" in command:
        d_index = command.index("-d")
        f_index = command.index("-f")
        if d_index < f_index:
            create_dirs(command[d_index + 1:f_index])
            create_file(command[-1])
        else:
            create_dirs(command[d_index + 1:])
            create_file(command[f_index + 1])
    elif "-d" in command:
        start_index = command.index("-d")
        create_dirs(command[start_index + 1:])
    elif "-f" in command:
        create_file(command[-1])
