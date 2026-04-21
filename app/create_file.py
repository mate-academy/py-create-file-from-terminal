import datetime
import os
import sys


def create_directory(directories: list) -> str:
    path_dir = os.path.join(*directories)
    os.makedirs(path_dir)
    return path_dir


def create_file(file_name: str, path_dir: list) -> None:
    file_path = file_name
    if path_dir:
        dirs = create_directory(path_dir)
        file_path = os.path.join(dirs, file_path)
    current = datetime.datetime.now()
    with open(file_path, "a") as source_file:
        source_file.write(f"{current.strftime('%Y-%m-%d %H:%M:%S')}\n")
        while True:
            new_line = input("Enter content line: ")
            if new_line == "stop":
                break
            source_file.write(f"{new_line}\n")


def main() -> None:
    args = sys.argv
    directory_list = []
    file_name = ""
    directories_flag = False
    files_flag = False
    for arg in args:
        if directories_flag and not arg.startswith("-"):
            directory_list.append(arg)
        if files_flag and not arg.startswith("-"):
            file_name = arg
        if arg == "-d":
            directories_flag = True
            files_flag = False
        if arg == "-f":
            files_flag = True
            directories_flag = False
    if directory_list and not file_name:
        create_directory(directory_list)
    if file_name:
        create_file(file_name, directory_list)


if __name__ == "__main__":
    main()
