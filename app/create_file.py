import os
import sys
from datetime import datetime


def create_file_from_terminal() -> None:
    command_list = sys.argv
    path_list = []
    path = ""
    file_name = ""

    for index in range(len(command_list)):
        if command_list[index] == "-d":
            for next_index in range(index + 1, len(command_list)):
                if command_list[next_index] == "-f":
                    break
                path_list.append(command_list[next_index])

        try:
            if command_list[index] == "-f":
                file_name = command_list[index + 1]
        except IndexError:
            print("File name should be written after '-f'")
            return

    if len(path_list) > 0:
        path = os.path.join(*path_list)

    create_directory(path)

    if len(file_name) > 0:
        write_in_file(path, file_name)


def create_directory(path: str) -> None:
    if len(path):
        try:
            os.makedirs(path)
        except FileExistsError:
            return


def write_in_file(path: str, file_name: str) -> None:
    if len(path):
        try:
            modified_file = open(f"{path}/{file_name}", "a")
        except IOError:
            print(f"Path {path}/ does not exists")
            return
    else:
        modified_file = open(file_name, "a")

    modified_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    count_lines = 0
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            modified_file.write("\n")
            break
        count_lines += 1
        modified_file.write(f"{count_lines} {line}\n")

    modified_file.close()


create_file_from_terminal()
