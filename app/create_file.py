import os
import datetime


def create_file(new_file: str) -> None:
    result_name_file = new_file.split()
    if "python" == result_name_file[0]:
        for index in range(len(result_name_file)):
            if result_name_file[index] == "-d":
                create_dir(result_name_file, index)
            if result_name_file[index] == "-f":
                write_data_in_file(result_name_file, index)


def for_duplicate(directories: list[str]) -> None:
    for directory in directories:
        if os.path.exists(directory) is False:
            os.mkdir(directory)


def create_dir(result_name_file: list[str], index: int) -> None:
    for index_f in range(len(result_name_file)):
        if "-f" in result_name_file:
            if result_name_file[index_f] == "-f":
                directories = result_name_file[index + 1: index_f]
                for_duplicate(directories)
        directories = result_name_file[index + 1:]
        for_duplicate(directories)


def write_data_in_file(result_name_file: list[str], index: int) -> None:
    new_line_file = ""
    count = 0
    name_file = "".join(result_name_file[index + 1:])
    with open(name_file, "w") as source_file:
        time_now = datetime.datetime.now()
        source_file.write(time_now.strftime("%Y-%m-%d %H:%M:%S"))
        while "stop" != new_line_file:
            new_line_file = input("Enter content line: ")
            count += 1
            if "stop" == new_line_file:
                break
            source_file.write(f"\n{count} "
                              f"Line{count} {new_line_file}")


create_file("python create_file.py -d dir1 dir2")
