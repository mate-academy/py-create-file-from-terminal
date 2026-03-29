import os
import datetime
import sys


def create_dir(path_dir: str) -> None:
    os.makedirs(path_dir, exist_ok=True)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        line_number = 1
        now = datetime.datetime.now()
        file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            file.write(f"{line_number} {new_line} \n")
            line_number += 1
        file.write("\n")


def create_dir_and_file(command: list) -> None:
    path_dir = os.path.abspath(os.curdir)
    if "-d" in command and "-f" in command and\
            command.index("-d") < command.index("-f"):
        for directory in command[command.index("-d") + 1:command.index("-f")]:
            path_dir = os.path.join(path_dir, directory)
        file_name = command[-1]
        create_dir(path_dir)
        create_file(os.path.join(path_dir, file_name))
    elif "-d" in command and "-f" in command:
        for directory in command[command.index("-d") + 1:]:
            path_dir = os.path.join(path_dir, directory)
        file_name = command[2]
        create_dir(path_dir)
        create_file(os.path.join(path_dir, file_name))
    elif "-f" in command:
        file_name = command[-1]
        create_file(file_name)
    elif "-d" in command:
        for directory in command[command.index("-d") + 1:]:
            path_dir = os.path.join(path_dir, directory)
        create_dir(path_dir)


if __name__ == "__main__":
    create_dir_and_file(sys.argv)
