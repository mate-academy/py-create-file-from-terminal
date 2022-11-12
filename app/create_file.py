import os
import sys
import datetime


def create_file(name_file: str) -> None:
    #new_file = sys.argv
    result_name_file = name_file.split()
    if "-d" in result_name_file and "-f" in result_name_file:
        index = result_name_file.index("-d")
        second_index = result_name_file.index("-f")
        create_directories_with_f(result_name_file, index)
        write_data_in_file(result_name_file, second_index)
    if "-d" in result_name_file and "-f" not in result_name_file:
        index = result_name_file.index("-d")
        create_directories(result_name_file, index)
    if "-f" in result_name_file and "-d" not in result_name_file:
        second_index = result_name_file.index("-f")
        write_data_in_file(result_name_file, second_index)


def for_duplicate(directories: list[str]) -> None:
    directory = "/".join(directories)
    if os.path.exists(directory) is False:
        os.makedirs(directory)


def create_directories_with_f(result_name_file: list[str], index: int) -> None:
    index_f = result_name_file.index("-f")
    directories = result_name_file[index + 1: index_f]
    for_duplicate(directories)


def create_directories(result_name_file: list[str], index: int) -> None:
    directories = result_name_file[index + 1:]
    for_duplicate(directories)


def write_data_in_file(result_name_file: list[str], second_index: int) -> None:
    new_line_file = ""
    count = 0
    name_file = "".join(result_name_file[second_index + 1:])
    with open(name_file, "a") as source_file:
        time_now = datetime.datetime.now()
        source_file.write(time_now.strftime("%Y-%m-%d %H:%M:%S\n"))
        while "stop" != new_line_file:
            new_line_file = input("Enter content line: ")
            count += 1
            if "stop" == new_line_file:
                break
            source_file.write(f"{count} "
                              f"Line{count} {new_line_file}\n")


create_file("python create_file.py -d dir1 dir2 -f file.txt")
