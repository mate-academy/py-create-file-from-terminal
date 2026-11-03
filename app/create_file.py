import os
import sys
import datetime


def catch_names_dir(args_list: list) -> list:
    result_list = []
    args_iterator = iter(args_list)
    try:
        while next(args_iterator) != "-d":
            pass
        while True:
            item = next(args_iterator)
            if item == "-f":
                break
            result_list.append(item)
    except StopIteration:
        pass
    return result_list


def create_path(name_dir: list) -> str:
    path = os.path.join(*name_dir)
    os.makedirs(path)
    return path


def catch_name(args_list: list) -> str:
    result = ""
    args_iterator = iter(args_list)
    try:
        while next(args_iterator) != "-f":
            pass
        result = next(args_iterator)
    except StopIteration:
        pass
    return result


args_list = sys.argv[1:]
if "-d" in args_list:
    name_dir = catch_names_dir(args_list)
    path_to_directory = create_path(name_dir)
if "-f" in args_list:
    file_name = catch_name(args_list)
    if "-d" in args_list:
        full_path = os.path.join(path_to_directory, file_name)
    else:
        full_path = file_name

    exists = os.path.exists(full_path) and os.path.getsize(full_path) > 0

    with open(full_path, "a") as new_file:
        if exists:
            new_file.write("\n")
        current_datetime = datetime.datetime.now()
        new_file.write(current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
        new_file.write("\n")
        counter = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            new_file.write(f"{counter} {content}\n")
            counter += 1
