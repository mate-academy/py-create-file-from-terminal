import os
import sys
from datetime import datetime


def write_data(
        file_name: str,
        open_param: str,
        dirs_path: str = ""
) -> None:

    if dirs_path == "":
        create_path = file_name
    else:
        create_path = os.path.join(dirs_path, file_name)

    with open(create_path, open_param) as file:
        if open_param == "a":
            file.write("\n")
        current_date = datetime.now()
        file.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        nr_line = 0
        while True:
            nr_line += 1
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{nr_line} {content}" + "\n")


def create_file() -> None:
    command = sys.argv

    if "-f" in command and "-d" not in command:
        file_name = command[command.index("-f") + 1]
        if os.path.exists(file_name):
            write_data(file_name, "a")
        else:
            write_data(file_name, "w")
    elif "-d" in command and "-f" not in command:
        list_of_dirs = [dirs for dirs in command[2:]]
        dirs_path = os.path.join(*list_of_dirs)

        if not os.path.exists(dirs_path):
            os.makedirs(dirs_path)

    elif "-d" in command and "-f" in command:
        file_name = command[command.index("-f") + 1]
        index_f = command.index("-f")
        index_d = command.index("-d")

        if index_f < index_d:
            list_of_dirs = [dirs for dirs in command[index_d + 1::]]
        else:
            list_of_dirs = [dirs for dirs in command[2:index_f]]

        if list_of_dirs:
            dirs_path = os.path.join(*list_of_dirs)
            os.makedirs(dirs_path)
        else:
            dirs_path = "."

        if os.path.exists(os.path.join(str(dirs_path), file_name)):
            write_data(file_name, "a", str(dirs_path))
        else:
            write_data(file_name, "w", str(dirs_path))


create_file()
