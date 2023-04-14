import sys
import os

from datetime import datetime


def create_file(name_file: str) -> None:
    if os.path.exists(name_file):
        flag = "a"
    else:
        flag = "w"
    with open(name_file, flag) as file:
        if flag == "w":
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        else:
            file.write("\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line = ""
        while line != "stop":
            line = input("Enter content line: ")
            if line != "stop":
                file.write("\n" + line)
                line = ""
        file.write("\n")


def create_dirs(path_dir: list) -> None:
    path = os.path.join(*path_dir)
    os.makedirs(path, exist_ok=True)
    os.chdir(path)


if __name__ == '__main__':
    command = sys.argv
    if "-d" in command:
        start_index = command.index("-d")
        if "-f" not in command:
            create_dirs(command[start_index + 1:])
        else:
            finish_index = command.index("-f")
            create_dirs(command[start_index + 1:finish_index])
            create_file(command[-1])
    elif "-f" in command:
        create_file(command[2])
