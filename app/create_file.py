import os
import sys
from datetime import datetime


def unpack_argv() -> tuple[list[str], str]:
    directory_path_structure = []
    file_name = ""
    flag_dir = False
    flag_name = False
    for arg in sys.argv:
        if "-d" == arg:
            flag_dir = True
            flag_name = False
            continue
        if "-f" == arg:
            flag_name = True
            flag_dir = False
            continue
        if flag_dir:
            directory_path_structure.append(arg)
        if flag_name:
            file_name += arg
    return directory_path_structure, file_name


def creating_path() -> tuple[str, str]:
    dir_path_components, file_name = unpack_argv()
    dir_path = os.path.join(os.getcwd(), *dir_path_components)
    f_path = os.path.join(dir_path, file_name)
    return dir_path, f_path


def creation_file(content_file_path: str) -> None:
    with open(content_file_path, "a") as result_file:
        result_file.write(
            f"{str(datetime.now().strftime('%y-%m-%d %H:%M:%S'))}\n"
        )
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            result_file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    directory_path, file_path = creating_path()
    os.makedirs(directory_path, exist_ok=True)

    if directory_path != file_path[:-1]:
        creation_file(file_path)


if __name__ == "__main__":
    main()
