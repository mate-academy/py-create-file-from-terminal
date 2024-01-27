import sys
import os
from datetime import datetime


def create_file(list_of_dirs: list[str], filename: str) -> None:
    print("filename", filename)
    if filename == "":
        path_for_dirs = os.path.join(*list_of_dirs)
        os.makedirs(path_for_dirs, exist_ok=True)
        return
    if len(list_of_dirs) > 0:
        path_for_file = os.path.join(*list_of_dirs)
        os.makedirs(path_for_file, exist_ok=True)
        path_for_file = os.path.join(*list_of_dirs, filename)
    else:
        path_for_file = filename

    with open(path_for_file, "a") as a:
        a.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        user_data_line = input("Enter content line: ")
        counter = 1

        while user_data_line.lower() != "stop":
            a.write(f"{counter} {user_data_line}\n")
            counter += 1
            user_data_line = input("Enter content line: ")

        a.write("\n")


def create_list_dirs(list_of_command: list[str]) -> list[str]:
    current_dirs = []
    for el in list_of_command:
        if el == "-f":
            break
        current_dirs.append(el)
    return current_dirs


commands_list = sys.argv[1:]

if "-d" in commands_list and "-f" in commands_list:
    user_file = commands_list[commands_list.index("-f") + 1:][0]

    dirs = create_list_dirs(commands_list[1:])
    create_file(dirs, user_file)
elif "-d" in commands_list:
    dirs = create_list_dirs(commands_list[1:])
    create_file(dirs, "")
elif "-f" in commands_list:
    user_file = commands_list[commands_list.index("-f") + 1:][0]
    create_file([], user_file)
else:
    create_file(["dir1", "dir2"], "file.txt")
