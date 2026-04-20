from datetime import datetime
import os
from sys import argv


def check_command_from_terminal(info: list) -> None:
    command = [value for value in info if "-" in value]
    if len(command) < 2:
        if command[0] == "-f":
            work_with_file(info[-1])
        else:
            create_dirs(info[2:])
    else:
        file_name = info[-1]
        folder = create_dirs(info[2:-2])
        work_with_file(os.path.join(folder, file_name))


def work_with_file(name: str) -> None:
    with open(name, "a") as new_file:
        line_number = 1
        print(datetime.strftime(datetime.now(), "%y-%m-%d %H:%M:%S"),
              file=new_file)
        while True:
            word = input("Enter content line: ")
            if word == "stop":
                break
            print(line_number, word, file=new_file)
            line_number += 1


def create_dirs(dirs_name: list) -> str:
    full_dirs = os.path.join(*dirs_name)
    if not os.path.exists(full_dirs):
        os.makedirs(full_dirs)
    return full_dirs


if __name__ == "__main__":
    check_command_from_terminal(argv)
