import sys
import os
import datetime


def write_in_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                file.write("\n")
                break
            file.write(f"{line_num} {line}\n")
            line_num += 1


def find_path_and_create_file() -> None:
    command = sys.argv
    parent_dir = os.getcwd()

    if "-f" in command:
        file_path = command[command.index("-f") + 1]
        if "-d" in command:
            directories_list = command[2:-2] \
                if command.index("-d") == 1 \
                else command[command.index("-d") + 1:]
            to_join = os.path.sep.join(directories_list)
            to_join_all = os.path.join(parent_dir, to_join)
            os.makedirs(to_join_all, exist_ok=True)
            file_path = os.path.join(to_join_all, file_path)
        write_in_file(file_path)
    if "-d" in command and "-f" not in command:
        directories_list = command[2:]
        to_join = os.path.sep.join(directories_list)
        to_join_all = os.path.join(parent_dir, to_join)
        os.makedirs(to_join_all, exist_ok=True)


find_path_and_create_file()
