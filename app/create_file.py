import sys
import os
import datetime


def check_flag(flag: str, source_array: list) -> bool:
    return True if flag in source_array else False


def get_directories(source_array: list, with_file: bool) -> list:
    directories = []
    last_index = len(source_array)
    if with_file:
        last_index = source_array.index("-f")
    for i in range(source_array.index("-d") + 1, last_index):
        directories.append(source_array[i])
    return directories


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def get_file_name(source_array: list) -> str:
    return source_array[source_array.index("-f") + 1]


def get_file_path(
        file_name: str,
        within_directory: bool,
        path: str = "") -> str:
    return os.path.join(path, file_name) if within_directory else file_name


def create_file(file_path: str) -> None:
    with open(file_path, "a") as source_file:
        source_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        user_input = input("Enter content line: ")
        line_number = 1
        while user_input != "stop":
            source_file.write(f"{line_number} {user_input}\n")
            line_number += 1
            user_input = input("Enter content line: ")
        source_file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")


flag_directories = check_flag("-d", sys.argv)
flag_file = check_flag("-f", sys.argv)

if flag_directories:
    path = create_path(get_directories(sys.argv, flag_file))
    if not os.path.exists(path):
        os.makedirs(path)

if flag_file:
    file_path = get_file_path(
        get_file_name(sys.argv),
        flag_directories,
        create_path(
            get_directories(sys.argv, flag_file)) if flag_directories else "")
    create_file(file_path)
