import os
from sys import argv
from datetime import datetime


def get_flags_dict() -> dict:
    dict_of_flags = {"-d": None, "-f": None}

    try:
        index_d = argv.index("-d")
    except ValueError:
        index_d = False

    try:
        index_f = argv.index("-f")
    except ValueError:
        index_f = False

    if index_f and index_d:
        if index_f > index_d:
            arguments_d = argv[index_d + 1:index_f]
            arguments_f = argv[index_f + 1:]
        else:
            arguments_d = argv[index_d + 1:]
            arguments_f = argv[index_f + 1: index_d]
        dict_of_flags["-d"] = arguments_d
        dict_of_flags["-f"] = arguments_f
    elif index_d:
        arguments_d = argv[index_d + 1:]
        dict_of_flags["-d"] = arguments_d
    elif index_f:
        arguments_f = argv[index_f + 1:]
        dict_of_flags["-f"] = arguments_f

    return dict_of_flags


def create_files_and_folders() -> None:
    if dict_with_flags["-d"]:
        folders_to_create = os.path.join(*dict_with_flags["-d"])
        os.makedirs(folders_to_create)
    if dict_with_flags["-f"]:
        path_to_file = os.path.join(*dict_with_flags['-f'])
        if dict_with_flags["-d"]:
            path_to_file = os.path.join(folders_to_create, *dict_with_flags['-f'])
        with open(path_to_file, "w") as file:
            date_time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{date_time_now}\n")
            counter = 0
            while True:
                counter += 1
                user_input = input("Enter content line: ")
                if user_input == "stop":
                    break
                file.write(f"{counter} {user_input}\n")


if __name__ == "__main__":
    dict_with_flags = get_flags_dict()
    create_files_and_folders()
