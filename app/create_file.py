import sys
import os
from datetime import datetime


class InvalidCommandError(Exception):
    pass


def make_file(file_path: str) -> None:
    with open(file_path, "a") as new_file:
        current_date = datetime.now()
        new_file.write(current_date.strftime("%Y-%m-%d % %H:%M:%S"))
        lines_list = []
        while sys.argv != "stop":
            sys.argv = input("Enter content line: ")
            lines_list.append(sys.argv)
        for i in range(len(lines_list) - 1):
            new_file.writelines("\n")
            new_file.writelines(str(i + 1))
            new_file.writelines(" ")
            new_file.writelines(lines_list[i])
        new_file.write("\n")


def create_file() -> None:
    create_path = input()
    create_path = create_path.split()

    if "-d" in create_path and "-f" in create_path:
        index_d = create_path.index("-d")
        index_f = create_path.index("-f")
        dirs = os.path.join(*create_path[index_d + 1: index_f])
        file_name = create_path[index_f + 1]
        path = os.path.join(dirs, file_name)
        os.makedirs(dirs, exist_ok=True)
        make_file(path)

    elif "-f" in create_path:
        index_f = create_path.index("-f")
        file_name = create_path[index_f + 1]
        make_file(file_name)

    elif "-d" in create_path:
        index_d = create_path.index("-d")
        dirs = os.path.join(*create_path[index_d + 1:])

        os.makedirs(dirs, exist_ok=True)

    else:
        raise InvalidCommandError("Invalid command specified")


create_file()
