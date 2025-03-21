import os
import sys
from datetime import datetime


def create_directory(path_parts: list) -> None:
    directory_path = os.path.join(*path_parts)
    normpath = directory_path.replace("\\", "/")
    if not os.path.exists(normpath):
        os.makedirs(normpath)


def create_file(file_name: str) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a") as f:
        f.write(f"{str(current_time)}\n")

    with open(file_name, "a") as f:
        line_number = 1
        while True:
            user_input = input(str(f"Enter content line: {line_number} "))
            if user_input == "stop":
                break
            f.write(f"{line_number} Line{line_number} {user_input}\n")
            line_number += 1


def main() -> None:
    file_name = ""
    path_parts = []
    only_arguments = sys.argv[1:]
    for i, arg in enumerate(only_arguments):
        if "-d" in only_arguments and "-f" not in only_arguments:
            if arg != "-d":
                path_parts.append(arg)
        if "-d" in only_arguments and "-f" in only_arguments:
            if arg != "-f" and arg != "-d" and ".txt" not in arg:
                path_parts.append(arg)
        if arg[0] == "-f":
            create_file(only_arguments[-1])
        if ".txt" in arg:
            file_name = arg
    if only_arguments[0] == "-d":
        create_directory(path_parts)
    if "-f" in only_arguments:
        filename = os.path.join(*path_parts, file_name)
        normpath_file = filename.replace("\\", "/")
        create_file(normpath_file)


if __name__ == "__main__":
    main()
