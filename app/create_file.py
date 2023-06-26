import os
from sys import argv
from datetime import datetime


def recieve_command_form_console_and_make_a_dict_of_flags() -> dict:
    dict_of_flags = {"-d": None, "-f": None}
    splited_command = argv

    try:
        indedx_d = splited_command.index("-d")
    except ValueError:
        indedx_d = False

    try:
        indedx_f = splited_command.index("-f")
    except ValueError:
        indedx_f = False

    if indedx_f and indedx_d:
        arguments_d = splited_command[indedx_d + 1:indedx_f]
        arguments_f = splited_command[indedx_f + 1:]
        dict_of_flags["-d"] = arguments_d
        dict_of_flags["-f"] = arguments_f
    elif indedx_d:
        arguments_d = splited_command[indedx_d + 1:]
        dict_of_flags["-d"] = arguments_d
    elif indedx_f:
        arguments_f = splited_command[indedx_f + 1:]
        dict_of_flags["-f"] = arguments_f

    return dict_of_flags


def create_files_and_folders() -> None:
    if dict_with_flags["-d"]:
        folders_to_create = "/".join(dict_with_flags["-d"])
        os.makedirs(folders_to_create)
    if dict_with_flags["-f"]:
        way_to_file = f"./{''.join(dict_with_flags['-f'])}"
        if dict_with_flags["-d"]:
            way_to_file = (f"./{folders_to_create}/"
                           f"{''.join(dict_with_flags['-f'])}")
        with open(way_to_file, "w") as file:
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
    dict_with_flags = recieve_command_form_console_and_make_a_dict_of_flags()
    create_files_and_folders()
